//
// Created by LanCher on 25-4-5.
//

#pragma once

#include <utility>
#include <vector>
#include <unordered_map>
#include <string>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <iostream>
#include <iomanip>

// #include "Test/LanCherLogger.h"
using namespace std;

enum SymbolType { SYMBOL_INT, SYMBOL_FLOAT, SYMBOL_FUNCTION };

// 一个符号
struct Symbol {
    string name;

    SymbolType type; // 0: int, 1: float ,2: function
    bool isUsed = false; // 用于检查未使用的变量
    bool isConst = false; // 是否为常量
    int col, row; // 用于输出错误信息
    // only 函数 
    vector<SymbolType> params; // 函数参数列表，检测形参和实参个数是否匹配。你说得对，虽然可以只用一个数字来表示个数，但是我先用字符串来表示函数参数类型，方便后续扩展
    Symbol() = default;
    // 为了方便变量定义
    Symbol(const string& name, const SymbolType type, const int row, const int col, const bool isConst = false) {
        this->name = name;
        this->type = type;
        this->isConst = isConst;
        this->row = row;
        this->col = col;
    }
    // 为了方便函数定义
    Symbol(const string& name, const vector<Symbol>& params, const int row, const int col) {
        this->name = name;
        this->params.reserve(params.size());
        for (const auto& param : params) {
            this->params.push_back(param.type);
        }
        this->type = SYMBOL_FUNCTION;
        this->row = row;
        this->col = col;
    }
};

// 符号表类
class SymbolTable {
    vector<unordered_map<string, Symbol>> scopes;

    // 工具：变量名统一转小写
    static string normName(const string& name) {
        string res = name;
        for (auto& c : res) c = tolower(c);
        return res;
    }

public:
    SymbolTable() {
        enterScope(); // 全局作用域
    }

    void enterScope() {
        scopes.push_back({});
    }

    void exitScope() {
        if (!scopes.empty()) {
            for (const auto& pair : scopes.back()) {
                const string& name = pair.first;
                const Symbol& sym = pair.second;
                // 只对变量和常量做未使用检查，不对函数/类型/关键字/错误token做未使用检查
                if (sym.type != SYMBOL_FUNCTION
                    && name != "int" && name != "float"
                    && name != "const" && name != "def"
                    && name != "begin" && name != "end"
                    && name != "call" && name != "let"
                    && name != "if" && name != "then"
                    && name != "else" && name != "fi"
                    && name != "while" && name != "do"
                    && name != "endwh" && name != "return"
                    && name != "and" && name != "or"
                    && !name.empty() && isalpha(name[0])
                    && !sym.isUsed) {
                    cerr << "语义警告: 变量 '" << sym.name << "' 定义但未使用, 在 (" << sym.row << "," << sym.col << ")\n";
                }
            }
            scopes.pop_back();
        }
    }

    bool addSymbol(Symbol symbol) {
        // 变量名、函数名统一小写
        string name = symbol.type == SYMBOL_FUNCTION
            ? makeSignature(normName(symbol.name), static_cast<int>(symbol.params.size()))
            : normName(symbol.name);
        symbol.name = normName(symbol.name); // 保证输出时原始名
        auto& currentScope = scopes.back();
        if (currentScope.count(name)) {
            const auto& existingSymbol = currentScope[name];
            if (symbol.type == SYMBOL_FUNCTION) {
                cerr << "语义错误: 函数 '" << symbol.name << "' 重复定义, 原有的位于 (" << existingSymbol.row << "," << existingSymbol.col << "), 新定义的位于 (" << symbol.row << "," << symbol.col << ")\n";
            } else {
                cerr << "语义警告: 变量 '" << symbol.name << "' 重复定义, 原有的位于 (" << existingSymbol.row << "," << existingSymbol.col << "), 新定义的位于 (" << symbol.row << "," << symbol.col << ")\n";
            }
            return false;
        }
        currentScope[name] = symbol;
        return true;
    }

    Symbol* lookup(const string& name) {
        string norm = normName(name);
        for (auto it = scopes.rbegin(); it != scopes.rend(); ++it) {
            if (it->count(norm)) {
                return &(*it)[norm];
            }
        }
        return nullptr;
    }

    static string makeSignature(const string& name, int paramCount) {
        return name + "#" + to_string(paramCount);
    }
    Symbol* lookup(const string& funcName, int paramCount) {
        string sig = makeSignature(normName(funcName), paramCount);
        for (auto it = scopes.rbegin(); it != scopes.rend(); ++it) {
            if (it->count(sig)) return &(*it)[sig];
        }
        return nullptr;
    }

    void markUsed(const string& name, const int row, const int col, int paramCount = -1) {
        string norm = normName(name);
        Symbol* sym = paramCount < 0 ? lookup(norm) : lookup(norm, paramCount);
        if (sym) {
            sym->isUsed = true;
        } else {
            cerr << "语义错误: 使用了未声明的符号 '" << name
                << (paramCount >= 0 ? "#" + to_string(paramCount) : "")
                << "', 在 (" << row << "," << col << ")\n";
        }
    }

    bool checkFunctionCall(const string& funcName, const vector<SymbolType>& argTypes, const int row, const int col) {
        Symbol* sym = lookup(funcName, static_cast<int>(argTypes.size()));
        if (!sym) {
            cerr << "语义错误: 函数 '" << funcName << "' 未定义, 在 (" << row << "," << col << ")\n";
            return false;
        }
        if (sym->type != SYMBOL_FUNCTION) {
            cerr << "语义错误: '" << funcName << "' 不是函数, 在 (" << row << "," << col << ") ,曾作为 " << (sym->isConst ? "常量" : "变量") << " 定义, 位于 (" << sym->row << "," << sym->col << ")\n";
            return false;
        }
        if (sym->params.size() != argTypes.size()) {
            cerr << "语义错误: 函数 '" << funcName << "' 参数数量不匹配, 期望 " << sym->params.size() << " 个参数, 实际 " << argTypes.size() << " 个参数, 在 (" << row << "," << col << ")\n";
            return false;
        }
        return true;
    }
};