#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    ofstream MyFile;
    MyFile.open(example.txt);
    MyFile<<"Hello this is my first file"<<endl;
    MyFile.close();
}
