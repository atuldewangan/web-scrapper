# Push-Notification
##Problem
Design a push notification service, design class diagrams and relations between different entities. This push notification service should be able to 
Send push notification to a single device Send push notification to a user with multiple devices. Send push notification to groups (of users), (High Priority/ Low Priority) (one user can be in multiple groups)

## Instructions 

1.  Start this Application
    -  `mvn clean install`
    -  `mvn spring-boot:run`
    
2.  Create Users
    -   endpoint : `localhost:8080/users`
    -   Request Type : POST
    -   Body :      
           ```
            {
                    "name": "Atul Dewanagan",
                    "email": "atulDewanagan@gmail.com",
                    "devices": [
                                {
                                    "name": "OnePLus6T"
                                },
                                {
                                    "name": "IPhone 12s"
                                }
            
                    ],
                    "group": false
            }
        ```
    -   Response :
     
           ```
            {
                "id": 3,
                "name": "Atul Dewanagan",
                "email": "atulDewanagan@gmail.com",
                "devices": [
                    {
                        "id": 3,
                        "name": "OnePLus6T"
                    },
                    {
                        "id": 4,
                        "name": "IPhone 12s"
                    }
                ],
                "group": false
            }
        
          ```

3. Fetch list of all Users;
    -   endpoint : `localhost:8080/users`
    -   Request Type : GET
    -   Response :
         ```
        [
            {
                "id": 1,
                "name": "Atul",
                "email": "abc@gmail.com",
                "devices": [
                    {
                        "id": 1,
                        "name": "OnePLus5T"
                    }
                ],
                "group": false
            },
            {
                "id": 2,
                "name": "Atul Dewanagan",
                "email": "atulDewanagan@gmail.com",
                "devices": [
                    {
                        "id": 2,
                        "name": "OnePLus7T"
                    },
                    {
                        "id": 3,
                        "name": "IPhone 13s"
                    }
                ],
                "group": false
            }
        ]
        
         ```              
4.  Create Notification
    -   endpoint : `localhost:8080/notification`
    -   Request Type : POST
    -   Body :      
           ```
                {
                    "type": "email",
                    "priority": 1,
                    "data": "Notification Mesaage New Latest"
                }
        ```
    -   Response :
     
           ```
            {
                "id": 2,
                "type": "email",
                "priority": 1,
                "data": "Notification Mesaage New Latest"
            }
        
          ```

5. Fetch list of all Notification;

    -   endpoint : `localhost:8080/notification`
    -   Request Type : GET
    -   Response :
     
           ```
            [
                {
                    "id": 1,
                    "type": "email",
                    "priority": 1,
                    "data": "Notification Mesaage "
                },
                {
                    "id": 2,
                    "type": "email",
                    "priority": 1,
                    "data": "Notification Mesaage New Latest"
                }
            ]
        
          ```
  
6.  Send Notification to a user
    -   endpoint : `localhost:8080/notification/notify-user`
    -   Request Type : POST
    -   Body :      
            
         ```
                    {
                        "notificationId":4,
                         "userId": 2
                    }        
         ```
            
    -   Response :
         ```
                [
                    {
                        "message": "Notification Data"
                    }
                ]
         ```                

5. Corner Cases;
     - If a push notification is sent to both High/Low groups and some users are in both groups, those users should get only one  because before sending each notification, it will be checked in `NotificaitonHisotry`.
        