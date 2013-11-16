# To change this template, choose Tools | Templates
# and open the template in the editor.
from __future__ import with_statement

__author__="Xi Yu"
__date__ ="$2013-10-1 13:21:56$"

import csv
import BST
import nanotime

def open_csv(file):
   with open(file+".csv",'rb') as f:
       reader = csv.reader(f)
       rows = list(reader)
       return rows


def bst_initialize(choice, Data):
        tree = []
        for eachlist in Data:
            if tree == []:
              tree = BST.Node(BST.Data(eachlist[0],eachlist[1],eachlist[2],eachlist[3]))
            else:
              tree.insert(BST.Data(eachlist[0],eachlist[1],eachlist[2],eachlist[3]),choice)
        return tree

def cellphone_initialize(choice, Data):
        tree = []
        for eachlist in Data:
            if tree == []:
              tree = BST.Node(BST.Data(eachlist[0],eachlist[1],filter(str.isdigit, eachlist[2]),eachlist[3]))
            else:
              tree.insert(BST.Data(eachlist[0],eachlist[1],filter(str.isdigit, eachlist[2]),eachlist[3]),choice)
        return tree        
    

if __name__ == "__main__":
    print "Please select FILE you want to search for"
    Filename = raw_input()
    RowData = open_csv(file = Filename)
    
#BST creating
    print "System Processing..."
    firstname_tree = bst_initialize("first_name", RowData)
    lastname_tree = bst_initialize("last_name", RowData)
    cellphone_tree = cellphone_initialize("cell_phone", RowData)
    cityname_tree = bst_initialize("city_name", RowData)
        
#Search BST start
    while True:
        print "What would you like to search on? (F,L,P,C)"
        DataChoice = raw_input()
        if DataChoice.lower() == "f":
            print "Enter the partial First Name"
            F_input = raw_input() 
            print "Result: FIRST NAME |  LAST NAME  |   CELLPHONE   |  CITY NAME"
            c_start = int(nanotime.now())
            count = firstname_tree.lookup_no_recursive(F_input.capitalize(),"first_name")
            print "(",count,"total matches",")"
            c_end = int(nanotime.now())
            print (c_end - c_start)/1000000,"ms"
        elif DataChoice.lower() == "l":
            print "Enter the partial Last Name"
            L_input = raw_input()
            print "Result: FIRST NAME  |  LAST NAME  |   CELLPHONE   |  CITY NAME"
            c_start = int(nanotime.now())
            count = lastname_tree.lookup_no_recursive(L_input.capitalize(),"last_name")
            c_end = int(nanotime.now())
            print (c_end - c_start)/1000000,"ms"
            print "(",count,"total matches",")"
        elif DataChoice.lower() == "p":
            print "Enter the cellphone number (digital only)"
            P_input = raw_input()
            print "Result: FIRST NAME  |  LAST NAME  |   CELLPHONE   |  CITY NAME"
            c_start = int(nanotime.now())
            count = cellphone_tree.lookup_no_recursive(P_input,"cell_phone")
            c_end = int(nanotime.now())
            print (c_end - c_start)/1000000,"ms"
            print "(",count,"total matches",")"
        elif DataChoice.lower() == "c":
            print "Enter the partial city name"
            C_input = raw_input() 
            print "Result: FIRST NAME  |  LAST NAME  |   CELLPHONE   |  CITY NAME"
            c_start = int(nanotime.now())
            count = cityname_tree.lookup_no_recursive(C_input.capitalize(),"city_name")
            c_end = int(nanotime.now())
            print (c_end - c_start)/1000000,"ms"
            print "(",count,"total matches",")"
        else:
            print "Input is wrong, please import exact elements inside of parenthesis"
        print "Another Search? (Y,N)"
        New_Search = raw_input()
        if New_Search.lower() == "n":
         break
        if New_Search.lower() != "y":
         print "Sorry,Wrong Input, system closing"
         break
    print "Thank you for using the System.  By Xi Yu"
    

