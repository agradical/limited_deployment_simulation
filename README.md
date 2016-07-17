About:
    Simulation of deployment process of new big feature to the users with
    enabling the control over the limit on affected users.

Requirements:
    python 2.7
    Libraries: networkx, matplotlib

File Structure:
    classes/ : Folder contains all the class files for graph, user model
               and deployment
    main.py  : Main file to start the program
    users.dat: Data file which lists the teacher-student relationship

Usage:
    python main.py users.data

    Now program will prompt to ask for the node to start the deployment
    threshold number if any and if that limit to be followed strictly

    
