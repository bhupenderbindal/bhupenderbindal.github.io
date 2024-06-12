#include<stdio.h>
#include<iostream>
#include<fstream>
#include<vector>
#include<cmath>
#include<functional>
#include<map>

using namespace std;

void print_pattern(vector<string> pattern){
    for (auto it=pattern.begin(); it != pattern.end(); ++it){
        cout<<*it<<"\n";

    }
    
}
// CANNOT RETURN AN ARRAY OF UNKOWN SIZE IN C++
void mapper(string inputline, int res3[]){
    // map<char,int> mapper;
    // mapper['#']=0;
    // mapper['.']=1;
    vector<int> intvector;
    
    // for_each(inputline.begin(), inputline.end(),aa);
    // auto qq = map(aa, inputline);
    cout<<"original string"<<inputline<<"\n";
    // vector<int> first (6,100);
    // vector<int> second (4,100);
    // vector<int> res(first.size());
    array<int,5> first = { 2, 16, 77, 34, 50 };
    array<int,5> second = { 2, 16, 77, 34, 60 };
    array<int,first.size()> res;
    // int res[5];
    // fill_n(res.begin(), res.size(), 0);
    // transform (res.begin(), res.end(), first.begin(), second.begin(), std::plus<int>());
    for (int i=0; i<res.size(); ++i ){
        res[i]= first[i] - second[i];
    }
    // for ( auto it = res.begin(); it != res.end(); ++it ){
    //     // *it = 2;    
    //     std::cout << ' ' << *it;
    // }
    std::cout << '\n';

    // cout<<"addtion"<<res<<"\n";
    for (auto i: res){
        cout<<i<<" ";
    }
    std::cout << '\n';
    const int l =inputline.size();
    // WHY THE HELLL BELOW DOES NOT WORK
    // array<int,l> res2;
    int res2[l];

    for (int i=0; i<inputline.size(); ++i){
        // cout<<inputline.at(i);
        if (inputline.at(i)== '#'){
            cout<<'#'<<0;
            res3[i]=0;
        }
        if (inputline.at(i)== '.'){
            cout<<'.'<<1;
            res3[i]=1;

        }
        
    }

    std::cout << '\n';
}

// CANNOT RETURN AN ARRAY OF UNKOWN SIZE IN C++
void mapper2(string inputline, int res3[]){
    
    const int l =inputline.size();
    // WHY THE HELLL BELOW DOES NOT WORK
    // array<int,l> res2;
    int res2[l];

    for (int i=0; i<inputline.size(); ++i){
        if (inputline.at(i)== '#'){
            res3[i]=0;
        }
        if (inputline.at(i)== '.'){
            res3[i]=1;
        }        
    }

}

int arraydiff(int arr1[], int arr2[], int size){
    // const int l = (sizeof(arr1)/sizeof(*arr1));
    int res =0;
    for (int i=0; i <size; ++i){
        res += arr1[i]-arr2[i];

    }
    return res;
}

int main(){
    string x = "###....";
    string y = "###.#.#";
    const int l1 =x.size();
    const int l2 =y.size();
    int xint[l1], yint[l2];
    mapper2(x, xint);
    mapper2(y, yint);
    int diff = arraydiff(xint,yint, l1);
    cout<<"diff : "<<diff<<"\n";
    for (auto i:xint){
        cout<<i;
    }
}