# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 8:30:37 2015

@author: Mikalai Drabovich
"""
 
def robotize(well):
  return (ord(well[0])-ord('A'))*12+int(well[1:])-1
    
def humanize(well):
  return chr(ord('A')+int(well/12))+str(1+well%12)

'''
# code to generate human_values - too much typing otherwise :)
  for k in range(0,96):
      print '\''+map_test[k]+'\''+',',
      if (k+1)%12==0:
          print '\\'

# code to generate robot_values:)
  for k in range(0,96):
      print str(k)+',',
      if (k+1)%12==0:
          print '\\'  
          
'''

human_values = [\
'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12',\
'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12',\
'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12',\
'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12',\
'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'E11', 'E12',\
'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12',\
'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12',\
'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12']

robot_values = [
 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,\
 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,\
 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,\
 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47,\
 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,\
 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,\
 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,\
 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]


if __name__ == '__main__':        
  for i in range(0, 96):
      assert(humanize(i) == human_values[i])
      assert(robotize(human_values[i]) == i)
 
 