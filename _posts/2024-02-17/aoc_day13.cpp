#include<stdio.h>
#include<iostream>
#include<fstream>
#include<vector>
#include<cmath>
// #include<functional>
// #include<map>

using namespace std;

void mapper(string inputline, int res3[]){    
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
    int res =0;
    for (int i=0; i <size; ++i){
        // absolute is necessary
        res += abs(arr1[i]-arr2[i]);

    }
    return res;
}

void print_pattern(vector<string> pattern){
    for (auto it=pattern.begin(); it != pattern.end(); ++it){
        cout<<*it<<"\n";
    }
    
}

bool pattern_diff(vector<string> pattern_up, vector<string> pattern_down, int diff){
    int res = 0;
    int l = pattern_up.size();
    for (int i=0; i< l; ++i){
        int l1 =pattern_up.at(i).size();
        int l2 =pattern_down.at(l-i-1).size();
        int xint[l1], yint[l2];
        mapper(pattern_up.at(i), xint);
        mapper(pattern_down.at(l-i-1), yint);
        res += arraydiff(xint, yint, l1);
        
    }
    if (res == diff){
        return true;
    }
    else{
        return false;
    }
}

int findlor(vector<string> pattern, int diff){
    vector<string> pattern_up, pattern_down;
    int lor =0;
    int l = pattern.size();

    for(int i=0; i<l-1; i++){
        if (i >= floor(l/2)){

            int common_len = (l-i-1);
            //  pattern_even needs to be resized to accept elements; same for transform method
            pattern_up.resize(common_len);
            // instead of copy pattern-up can be defined here
            copy((pattern.end() -2*common_len), pattern.end()-common_len, pattern_up.begin());
            pattern_down.resize(common_len);
            copy(pattern.end()- common_len, pattern.end(), pattern_down.begin());
        }
        else{
            int common_len = (i+1);
            pattern_up.resize(common_len);
            copy(pattern.begin(), (pattern.begin()+common_len), pattern_up.begin());
            pattern_down.resize(common_len);
            copy((pattern.begin()+common_len), (pattern.begin()+2*common_len), pattern_down.begin());
        }
        if (pattern_diff(pattern_up, pattern_down,diff) == true ){
            return i+1;
        }
    }

    return 0;
}

vector<string> vectstrtranspose(vector<string> pattern, vector<string> patttranspose){
    int l = pattern.at(0).size();
    for (int i=0; i<l; ++i){
        string s="";
        for (auto line : pattern){
            s +=line.at(i);
        }
        patttranspose.push_back(s);
    }
    return patttranspose;
}

void solver(vector<vector<string>> all_patterns, int diff){
  
    int lor=0,lorsum=0;
    for (auto pattern: all_patterns){
        lor = findlor(pattern,diff);
        // cout<<"line of reflection  "<< lor<<"\n";

        lorsum +=100*lor;
        vector<string> patterntranspose;
        patterntranspose = vectstrtranspose(pattern, patterntranspose);

        lor = findlor(patterntranspose,diff);
        // cout<<"line of reflection  "<< lor<<"\n";

        lorsum +=1*lor;

    }
    cout<<"lorsum  "<< lorsum<<"\n";
  
}
int main()
{
 printf("This is code in c++.\n");
 
 ifstream inputfile("./input.txt");
 string s;
 vector<string> pattern;
 vector<vector<string>> all_patterns;
 while (getline(inputfile, s)){
    if (!s.empty()){
        // cout<<s;
        pattern.push_back(s);
    }
    else{
        all_patterns.push_back(pattern);
        pattern.clear();
    }
    
 }
 // for the last pattern
 all_patterns.push_back(pattern);
 cout<<"\n";

cout<<"total patterns: "<<all_patterns.size()<<"\n";
cout<<"part1: ";
solver(all_patterns, 0);
cout<<"part2: ";
solver(all_patterns, 1);
return 0;

}
