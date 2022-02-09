#include <iostream>
#include <queue>
#define ARRAYSIZE(A) sizeof(A)/sizeof((A)[0])
 
using namespace std;
 
priority_queue<int> smaller;
priority_queue<int, vector<int>, greater<int> > bigger;
 
int median(int a[], int size){
    int mid;
    smaller.push(a[0]); 
 
    for (int i = 1; i<size-1; i++){
        if(a[i] < smaller.top()){
            smaller.push(a[i]);}
        else{
            bigger.push(a[i]);}
        if(smaller.size() < bigger.size()){
            smaller.push(bigger.top());
            bigger.pop();}
        else if(smaller.size() > bigger.size() + 1){
            bigger.push(smaller.top());
            smaller.pop();}  
    }
     
    mid = smaller.top();
    return mid;  
}
 
int main()
{
    int Testcase;
    int Arr[200];
    int size = ARRAYSIZE(Arr);
     
    cin >> Testcase;
    for(int i = 0; i < Testcase; i++){cin >> Arr[i];}
    cout << median(Arr,size); 
}