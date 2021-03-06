from enum import Enum

class InstrumentType(Enum):
    '''
    Defines three types for musical instruments.
    '''
    PERCUSSION = 'p'
    STRINGS = 's'
    WIND = 'w'    

class Instrument:
    '''
    This defines a musical instrument with the name of
    the instrument and its classification.
    '''
    def __init__(self, name, classification):
        '''
        Creates a new instrument. The name and
        classification of the instrument are required
        parameters.
        '''
        self.name = name
        if isinstance(classification, InstrumentType):
            self.classification = classification
        else:
            raise ValueError("Invalid value for instrument type: {}".format(classification))

    def getClassification(self):
        '''
        Returns the classification of the musical instrument.
        '''
        return self.classification

    def getName(self):
        '''
        Returns the name of the musical instrument.
        '''
        return self.name

    def setClassification(self, classification):
        '''
        Sets the classification of the musical instrument.
        '''
        if isinstance(classification, InstrumentType):
            self.classification = classification
        else:
            raise ValueError("Invalid value for instrument type: {}".format(classification))

    def setName(self, name):
        '''
        Sets the name of the musical instrument.
        '''
        self.name = name

    def __gt__(self, other):
        '''
        Convenience function for comparison between
        instruments.
        '''
        return self.name > other.getName()

    def __lt__(self, other):
        '''
        Convenience function for comparison between
        instruments.
        '''
        return self.name < other.getName()

class SLLNode:
    '''
    This defines a node in a singly-linked list. The node
    contains a data component and a nextnode reference. By
    default, data and nextnode are None.
    '''
    def __init__(self, data=None, nextnode=None):
        '''
        Creates a new node in the singly-linked list. If
        there is no data or nextnode passed, the values
        default to None.
        '''
        self.data = data
        self.nextnode = nextnode

    def getData(self):
        '''
        Returns the object the node contains.
        '''
        return self.data

    def getNext(self):
        '''
        Returns the reference to the next node.
        '''
        return self.nextnode

    def setData(self, data):
        '''
        Sets the object the node contains.
        '''
        self.data = data

    def setNext(self, nextnode):
        '''
        Sets the reference to the next node.
        '''
        self.nextnode = nextnode

class SLList:
    '''
    INSTRUCTIONS: As a class, write the methods and the
    documentation for these for a fully-working
    singly-linked list.
    '''
    def __init__(self, head = None):
        '''
        Create an empty list if there is no node passed to
        the constructor. Otherwise, create a list with the
        node passed.
        '''
        self.head = head

    def countInstances(self, data):
        # Count the number of times
        #Contributor: Jared Dantis, Kyle Dulay
        times = 0
        if isinstance(data, SLLNode):
            currNode = self.head
            while currNode.getNext() is not None:
                if currNode.getData() == data.getData():
                    times += 1
                currNode = currNode.getNext()
                
            if currNode.getData() == data.getData():
                times += 1
        else:
            currNode = self.head
            while currNode.getNext() is not None:
                if currNode.getData() == data:
                    times += 1
                currNode = currNode.getNext()
                
            if currNode.getData() == data:
                times += 1
        return times

    def delete(self, data):
        '''
        Deletes the node and returns True if the node is
        found. If the node is not found in the list, the
        function returns False.
        '''
        #Contributor: Jared Dantis
        if isinstance(data, SLLNode):
            currNode = self.search(data.getData())
        else:
            currNode = self.search(data)
        if currNode is not None:
            currNode = currNode.getNext()
            return True
        return False

    def deleteAtHead(self):
        #Contributor: Jared Dantis
        if self.head is not None:
            self.head = self.head.getNext()

    def deleteAtTail(self):
        #Contributors: Jared Dantis, Kyle Dulay
        currNode = self.head
        if currNode is None:
            pass
        elif currNode.getNext() is None:
            self.head = None
        else:
            while currNode.getNext().getNext() is not None:
                currNode = currNode.getNext()
            currNode.setNext(None)

    def insert(self, data):
        '''
        Inserts a node at the end of the list.
        '''
        # @aureljared: whats the difference between this and insertAtTail() ???
        # @MysterEdge: My bad. This should have been clearer as a shorthand for insertAtTail.
        if isinstance(data, SLLNode):
            # insert more code here
            pass
        else:
            newNode = SLLNode(data)
        # insert more code here

    def insertAfter(self, data, newdata):
        # Look for the instance of data and add a new node
        # after it with newdata.

        #Contributor: Jared Dantis, Kyle Dulay
        
        currNode = self.search(data)
        if currNode is not None:
            if isinstance(newdata, SLLNode):
                newNode = newdata
            else:
                newNode = SLLNode(newdata)
            newNode.setNext(currNode.getNext())
            currNode.setNext(newNode)

    def insertBefore(self, data, newdata):
        # Look for the instance of data and add a new node
        # before it with newdata.

        #Contributor: Jared Dantis, Kyle Dulay
        currNode = self.head
        if currNode is not None:
            while currNode is not None and currNode.getNext().getData() != data:
                currNode = currNode.getNext()
            if currNode is None:
                #Insert an error statement
                pass
            elif isinstance(newdata, SLLNode):
                newdata.setNext(currNode.getNext())
                currNode.setNext(newData)
            else:
                newNode = SLLNode(newdata)
                newNode.setNext(currNode.getNext())
                currNode.setNext(newNode)

    def insertAtHead(self, data):
        '''
        Inserts a node at the start of the list.
        '''
        #Contributor: Jared Dantis, Kyle Dulay
        if isinstance(data, SLLNode):
            data.setNext(self.head)
            self.head = data
        else:
            newNode = SLLNode(data)
            newNode.setNext(self.head)
            self.head = newNode

    def insertAtTail(self, data):
        '''
        Inserts a node at the tail of the list.
        '''
        #Contributors: Jared Dantis, Kyle Dulay

        if isinstance(data, SLLNode):
            newNode = data
        else:
            newNode = SLLNode(data)
            
        if self.head is None:
            self.insertAtHead(newNode)
        else:
            currNode = self.head
            while currNode.getNext() is not None:
                currNode = currNode.getNext()
            currNode.setNext(newNode)

    def insertInOrder(self, data):
        # Insert a new node assuming that the list is in
        # ascending order and the order is preserved.

        #Contributors: Jared Dantis, Kyle Dulay
        if self.head is None:
            self.insertAtHead(SLLNode(data))
        else:
            currNode = self.head
            while currNode.getNext() is not None:
                if (currNode.getNext().getData() > data) and (currNode.getData() <= data):
                    nextNode = currNode.getNext()
                    dataNode = SLLNode(data)
                    currNode.setNext(dataNode)
                    dataNode.setNext(nextNode)
                    break
                else:
                    currNode = currNode.getNext()

    def getSize(self):
        '''
        Returns the number of elements in the list
        '''
        #Contributors: Clyde Jallorina, Kyle Dulay
        if self.head is None:
            return 0
        currNode = self.head
        count = 0
        while currNode.getNext() is not None:
            count += 1
            currNode = currNode.getNext()
        count += 1
        
        return count

    def search(self, data):
        # ValueError("Item {} not found".format(str(data)))
        # should be raised if the data is not found. If it
        # is found, the reference to the node is returned.

        #Contributors: Clyde Jallorina, Kyle Dulay
        if self.head is not None:
            if self.head.getData() == data:
                return self.head
            else:
                currNode = self.head
                while currNode.getNext() is not None:
                    if currNode.getData() == data:
                        return currNode
                    currNode = currNode.getNext()
                if currNode.getData() == data:
                    return currNode
        raise ValueError("Item {} not found".format(str(data)))

one = Instrument("Guitar", InstrumentType.STRINGS)
two = Instrument("Oboe", InstrumentType.WIND)
print(one < two)
