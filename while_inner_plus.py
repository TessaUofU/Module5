{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "5dd77877",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[9, 10]"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"\"\"\n",
    "Write a python program that, given an input list of any level of complexity/nestedness, will return the inner \n",
    "most list plus 1. This is to be done with a while loop. Note: the input will contain only integers or lists. \n",
    "\n",
    "As an example:\n",
    "\n",
    "input_list = [1,2,3,4,[5,6,7,[8,9]]]\n",
    "\n",
    "your_py_program.py input_list\n",
    "\n",
    "will produce:\n",
    "\n",
    "[9,10]\n",
    "\n",
    "That is [8, 9] (the inner most list) plus 1 -> [9, 10]\"\"\"\n",
    "\n",
    "def innerList(input_list):\n",
    "    \n",
    "    current_list = input_list\n",
    "    i = 0\n",
    "    list2 = []\n",
    "    \n",
    "    while True:\n",
    "        if i == len(current_list):\n",
    "            if current_list == input_list:\n",
    "                for m in range(len(input_list)):\n",
    "                    input_list[m] = input_list[m] + 1\n",
    "                    m +=1\n",
    "                    return input_list\n",
    "            else:\n",
    "                current_list = [x+1 for x in current_list]\n",
    "                return current_list\n",
    "        \n",
    "        for m in range(len(current_list)):\n",
    "            if isinstance(current_list[m], list):\n",
    "                current_list = current_list[m]\n",
    "                i = 0\n",
    "            else:\n",
    "                i += 1\n",
    "    \n",
    "input_list = [1,2,3,4,[5,6,7,[8,9]]]\n",
    "innerList(input_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5818d56b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2e5d8d08",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
