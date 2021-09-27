#!/usr/bin/python3
import webbrowser

new=2
tabUrl = "https://www.google.com/search?q="
term = input("Enter Search Char:- ")
webbrowser.open(tabUrl+term,new=new)