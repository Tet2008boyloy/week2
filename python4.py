{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "addc04a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.Rock,1.poper,2.scissor\n",
      "People show : 2\n",
      "Computer show: 1\n",
      "People Win\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "print (\"0.Rock,1.poper,2.scissor\")\n",
    "ppl = int(input(\"People show : \"))\n",
    "cp = random.randint(0,2)\n",
    "if cp==0:\n",
    "    print(\"Computer show: \" +str(cp))\n",
    "    if ppl == 0:\n",
    "        print (\"Draw\")\n",
    "    elif ppl == 1:\n",
    "        print(\"People Win\")\n",
    "    elif ppl == 2:\n",
    "        print(\"Computer Win\")\n",
    "    else:\n",
    "        print (\"NO Anser\")\n",
    "elif cp==1:\n",
    "    print(\"Computer show: \" +str(cp))\n",
    "    if ppl == 0:\n",
    "        print (\"Computer win\")\n",
    "    elif ppl == 1:\n",
    "        print(\"Draw\")\n",
    "    elif ppl == 2:\n",
    "        print(\"People Win\")\n",
    "    else:\n",
    "        print (\"NO Anser\")\n",
    "elif cp==2:\n",
    "    print(\"Computer show: \" +str(cp))\n",
    "    if ppl == 0:\n",
    "        print (\"People win\")\n",
    "    elif ppl == 1:\n",
    "        print(\"Computer Win\")\n",
    "    elif ppl == 2:\n",
    "        print(\"Draw\")\n",
    "    else:\n",
    "        print (\"NO Anser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3b34770e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
