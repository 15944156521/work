#include"lexicalAnalysis.h"
#include"grammaticalAnalysis.h"
#include <iostream>
#include <fstream>
#ifdef _WIN32
#include <windows.h>
#endif
using namespace std;
// 主函数
int main(int argc, char* argv[]) {
#ifdef _WIN32
    SetConsoleOutputCP(65001); // 设置控制台为UTF-8编码，适合VSCode终端
#endif
    std::ios::sync_with_stdio(false);

    if (argc < 2) {
        cerr << "参数错误: " << argv[0] << " <文件名>\n";
        return 1;
    }
    if (!initLexicalAnalysis(argv[1])) {
        cerr << "打开文件失败: " << argv[1] << endl;
        return 1;
    }

    Parser parser;
    vector<Quadruple> quadruples = parser.parse();
    Quadruple::printQuadruples(Quadruple::resolveLabels(quadruples));
    closeLexicalAnalysis();
    return 0;
}

