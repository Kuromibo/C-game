#include <iostream>
#include <cstdlib>
#include <ctime>


using namespace std;

int choice;
int index;

    
int gatcha(){
    cout << "do you want to pull?" << endl;
    cin >> choice;
    return choice;
}

int randint(){
    srand(time(0)); 
    index = 1+(rand()%3);
}

int main(){
    
    bool playerChoice = false;
    gatcha();
    
    // string OneStar[3] = {"Char1.1", "Char1.2", "Char1.3"};
    // string TwoStar[3] = {"Char2.1", "Char2.2", "Char2.3"};
    // string ThreeStar[3] = {"Char3.1", "Char3.2", "Char3.3"};
    int stars[] = {1, 2, 3};
    if(choice==0){
        playerChoice = true;
    }else if(choice==1){
        playerChoice = false;
    }

    if(playerChoice){
        randint();
        if(index==stars[0]){
        cout << "Char1.1" << endl;
        }else if(index==stars[1]){
        cout << "Char1.2" << endl;
        }else if(index==stars[2]){
        cout << "Char1.3" << endl;
        }
    }else if(!playerChoice){
        cout << gatcha();
    }
    

    return 0;
}
