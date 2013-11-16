# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="Xi Yu"
__date__ ="$2013-10-2 20:31:16$"

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


# insert function start---------------------------------------------------     
    def insert(self, data, column=None):
     if column == "first_name":
        if data.first_name < self.data.first_name:
            if  self.left is None:
                self.left = Node(data)
            else:
               self.left.insert(data, 'first_name')
        else:
             if self.right is None:
                self.right = Node(data)
             else:
                self.right.insert(data, 'first_name')
     elif column == "last_name":
         if data.last_name < self.data.last_name:
             if  self.left is None:
                 self.left = Node(data)
             else:
                self.left.insert(data, 'last_name')
         else:
              if self.right is None:
                 self.right = Node(data)
              else:
                 self.right.insert(data, 'last_name')
     elif column == "cell_phone":
         if data.cell_phone < self.data.cell_phone:
             if  self.left is None:
                 self.left = Node(data)
             else:
                self.left.insert(data, 'cell_phone')
         else:
              if self.right is None:
                 self.right = Node(data)
              else:
                 self.right.insert(data, 'cell_phone')
     elif column == "city_name":
         if data.city_name < self.data.city_name:
             if  self.left is None:
                 self.left = Node(data)
             else:
                self.left.insert(data, 'city_name')
         else:
              if self.right is None:
                 self.right = Node(data)
              else:
                 self.right.insert(data, 'city_name')
# insert function end---------------------------------------------------     
   
#
#    def insert(self, data):
#        if data.first_name < self.data.first_name:
#            if  self.left is None:
#                self.left = Node(data)
#            else:
#               self.left.insert(data)
#        else:
#             if self.right is None:
#                self.right = Node(data)
#             else:
#                self.right.insert(data)

    def print_tree(self):
      if self.left:
         self.left.print_tree()
      print self.data.first_name, self.data.last_name, self.data.cell_phone, self.data.city_name
      if self.right:
         self.right.print_tree()
     

    def lookup(self,data,parent = None):
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            print data


    def lookup_no_recursive (self,data,column,parent = None,count = 0):
        length = len(data)
        count = 0
        if column == "first_name":
            while self!= None:

                if cmp(data[0:length],self.data.first_name[0:length]) == 0:
    #            if data == self.data.first_name:
    #            if data in self.data.first_name:
    #                for subdata in self.tree_data():
    #                    if subtree == []:
    #                        subtree = Node(Data(subdata[0],subdata[1],subdata[2],subdata[3]))
    #                    else:
    #                        subtree.insert(Data(subdata[0],subdata[1],subdata[2],subdata[3]),"first_name")
                        count = self.tree_data(data,column)
                        break
                elif data < self.data.first_name:
                    self = self.left
                elif data > self.data.first_name:
                    self = self.right
            return count
        
        elif column == "last_name":
            while self!= None:
                if cmp(data[0:length],self.data.last_name[0:length]) == 0:
                        count = self.tree_data(data,column)
                        break
                elif data < self.data.last_name:
                    self = self.left
                elif data > self.data.last_name:
                    self = self.right
            return count
        
        elif column == "cell_phone":
            while self!= None:
                if cmp(data[0:length],self.data.cell_phone[0:length]) == 0:
                        count = self.tree_data(data,column)
                        break
                elif data < self.data.cell_phone:
                    self = self.left
                elif data > self.data.cell_phone:
                    self = self.right
            return count
          
        elif column == "city_name":
            while self!= None:
                if cmp(data[0:length],self.data.city_name[0:length]) == 0:
                        count = self.tree_data(data,column)
                        break
                elif data < self.data.city_name:
                    self = self.left
                elif data > self.data.city_name:
                    self = self.right
            return count
            
                    
    def tree_data(self,search,column, count = 0):
        length = len(search)
        stack = []
        node = self
        if column == "first_name":
            while stack or node:
              if node:
                 stack.append(node)
                 node = node.left
              else: # pop the node and print
                    node = stack.pop()
                    if search in node.data.first_name:
    #                if cmp(search[0:length],self.search.first_name[0:length]) == 0:
    #                if search == node.data.first_name:
                         count += 1
                         print "       ",node.data.first_name,"|", node.data.last_name,"|",node.data.cell_phone,"|", node.data.city_name
                    node = node.right
            return count

        elif column == "last_name":
            while stack or node:
              if node:
                 stack.append(node)
                 node = node.left
              else: 
                    node = stack.pop()
                    if search in node.data.last_name:
                         count += 1
                         print "       ",node.data.first_name,"|", node.data.last_name,"|",node.data.cell_phone,"|", node.data.city_name
                    node = node.right
            return count
        
        elif column == "cell_phone":
            while stack or node:
              if node:
                 stack.append(node)
                 node = node.left
              else:
                    node = stack.pop()
#                    if search in node.data.cell_phone:
                    if cmp(search[0:length],node.data.cell_phone[0:length]) == 0:
                         count += 1
                         print "       ",node.data.first_name,"|", node.data.last_name,"|", "(",node.data.cell_phone[0:3],")",node.data.cell_phone[3:6],"-",node.data.cell_phone[6:10],"|", node.data.city_name
                    node = node.right
            return count

        elif column == "city_name":
            while stack or node:
              if node:
                 stack.append(node)
                 node = node.left
              else: 
                    node = stack.pop()
                    if search in node.data.city_name:
                         count += 1
                         print "       ",node.data.first_name,"|", node.data.last_name,"|",node.data.cell_phone,"|", node.data.city_name
                    node = node.right
            return count


class Data:
    def __init__(self, first_name, last_name, cell_phone,city_name):
        self.first_name = first_name
        self.last_name = last_name
        self.cell_phone = cell_phone
        self.city_name = city_name




if __name__ == "__main__":
    print "Hello World"
