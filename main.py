import cmd
import mysql.connector
import pandas as pd

class MySqlClient:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host = "localhost",
            database = "SocialNetwork",
            user = "root",
            password = "password"
        )
        self.cursor = self.connection.cursor()
    
    def executeQuery(self, query, parameter = None):
        self.cursor.execute(query, parameter)

        return self.cursor
    
    def commit(self):
        self.connection.commit()
    
    def rollback(self):
        self.connection.rollback()

class SocialNetworkClient(cmd.Cmd):
    intro = 'Welcome to our social Network app.   Type help or ? to list commands.\n'
    prompt = '(social network) '
    
    def __init__(self):
        super(SocialNetworkClient, self).__init__()
        self.client = MySqlClient()
        self.current_userID = None


    def do_signup(self, arg):
        userName = input("Creat your user name: ")

        query = "insert into User (userName) values ('{}');".format(userName)
        self.client.executeQuery(query)
        self.client.commit()

        print("User {} has been created.".format(userName))


    def do_login(self, arg):
        userName = input("User name: ")

        query = "SELECT userID FROM User WHERE userName = '{}';".format(userName)
        results = self.client.executeQuery(query).fetchall()
        self.current_userID = results[0][0]

        if results:
            print("Login Successeed. Welcome, {}!".format(userName))
        else:
            print("Login Failed. User not found.")
			
    def do_logout(self, arg):
        print("You have been logged out!")
 	    self.current_userID = None


    def do_create_post(self, arg):
        topicTitle = input("Create your topic title: ")
        postTitle = input("Create your post title: ")
		text = input("Create your post text: ")

        try:
            if topic and content:
                topic_id = None
                query = "SELECT topicID FROM Topic WHERE topicTitle = '{}';".format(topicTitle)
                results = self.client.executeQuery(query).fetchall()
                if results:
                    topicID = result[0][0]
                    print("This topic does exist")
                else:
                    # Insert the topic if topic does not exist
                    query = "INSERT INTO Topic VALUES (%s, %s);"
                    parameter = (topic_id, topic)
                    topicID = self.client.executeQuery(query, parameter).lastrowid
                    print("The new topic has been created")
                # Insert the post with the topic
                if topicID;
                    query = "INSERT INTO Post (userID, postTitle, text) VALUES (%s, %s, %s);"
                    parameter = (self.current_userID, postTitle, text)
                    postID = self.client.executeQuery(query, parameter).lastrowid

                    # Insert into Post_Topic 
                    if postID:
                        query = "INSERT INTO Post_Topic VALUES (%s, %s);"
                        parameter = [postID, topicID]
                        self.client.executeQuery(query, parameter).lastrowid
                        self.client.commit()
        except mysql.connector.Error as error :
            print("Create post failed with error: {}".format(error))
            self.client.rollback()


    def do_create_group(self, arg):
        group_name = input("Input the group name: ")
        invitee_id = input("Input the invitee user ID: ")

        if not (group_name and invitee_id):
            print("Missing input. Create group failed")
            return

        try:
            create_group_query = "insert into `Group` (groupID, groupName) values (NULL, '{}', 2);".format(group_name)
            group_id = self.client.executeQuery(create_group_query).lastrowid

            # insert member in bulk
            insert_member_query = "insert into User_Group (userID, groupID) values (%s, %s);"
            params = [
                (group_id, self.current_userID),
                (group_id, int(invitee_id))
            ]

            self.client.cursor.executemany(insert_member_query, params)
            self.client.commit()
            print("You and user {} has join group {} successfully.".format(invitee_id, group_id))
        except mysql.connector.Error as error :
            print("Create group failed with error: {}".format(error))
            self.client.rollback()


    def do_follow_group(self, arg):
        group_id = input("Input the group ID: ")

        if not group_id:
            print("Missing input. Follow group failed")
            return

        try:
            find_group_query = "select * from `Group` where groupID = {}".format(group_id)
            result = self.client.executeQuery(find_group_query).fetchall()

            if not result:
                print("Group not found!")
            else:
                # follow group if group exist
                follow_group_query = "insert into User_Group (userID, groupID) values (%s, %s);"
                params = (group_id, self.current_userID)

                self.client.executeQuery(follow_group_query, params)
                self.client.commit()
                print("You have follow group {} successfully.".format(group_id))
        except mysql.connector.Error as error :
            print("Follow group failed with error: {}".format(error))
            self.client.rollback()


    def do_follow_topic(self, arg):
        topic_id = input("Input topic id: ")

        if not topic_id:
            print("Missing input. Follow topic failed.")
            return
        
        try:
            find_topic_query = "select * from Topic where topicID = {};".format(topic_id)
            result = self.client.executeQuery(find_topic_query).fetchall()

            if not result:
                print("Topic not found!")
            else:
                follow_topic_query = "insert into Subscribe_Topic values (%s, %s);"
                params = (topic_id, self.current_userID)

                self.client.executeQuery(follow_topic_query, params)
                self.client.commit()
                print("You have follow topic {} successfully.".format(topic_id))
        except mysql.connector.Error as error :
            print("Follow topic failed with error: {}".format(error))
            self.client.rollback()


    def do_follow_user(self, arg):
        followee_id = input("Input the id of the user you want to follow: ")

        if not followee_id:
            print("Missing input. Follow user failed!")
            return
        
        try:
            find_followee_query = "select * from User where userID = {};".format(followee_id)
            result = self.client.executeQuery(find_followee_query).fetchall()

            if not result:
                print("Followee not found")
            else:
                follow_user_query = "insert into User_Follower values (%s, %s);"
                params = (followee_id, self.current_userID)

                self.client.executeQuery(follow_user_query, params)
                self.client.commit()
                print("You have follow user {} successfully.".format(followee_id))
        except mysql.connector.Error as error :
            print("Follow user failed with error: {}".format(error))
            self.client.rollback()


    def do_thumbs_up(self, arg):
        post_id = input("Input post id: ")

        if not post_id:
            print("Missing input. Thumbs up failed")

        try:
            find_post_query = "select * from Post where postID = {};".format(post_id)
            result = self.client.executeQuery(find_post_query).fetchall()

            if not result:
                print("Post not found")
            else:
                thumbs_up_query = "update Post set thumbsUp = thumbsUp + 1 where postID = {};".format(post_id)

                self.client.executeQuery(thumbs_up_query)
                self.client.commit()
                print("You have thumbed up post {} successfully.".format(post_id))
        except mysql.connector.Error as error :
            print("Thumbs up failed with error: {}".format(error))
            self.client.rollback()
        
    
    def do_thumbs_down(self, arg):
        post_id = input("Input post id: ")

        if not post_id:
            print("Missing input. Thumbs down failed")

        try:
            find_post_query = "select * from Post where postID = {};".format(post_id)
            result = self.client.executeQuery(find_post_query).fetchall()

            if not result:
                print("Post not found")
            else:
                thumbs_down_query = "update Post set thumbsDown = thumbsDown + 1 where postID = {};".format(post_id)

                self.client.executeQuery(thumbs_down_query)
                self.client.commit()
                print("You have thumbed down post {} successfully.".format(post_id))
        except mysql.connector.Error as error :
            print("Thumbs down failed with error: {}".format(error))
            self.client.rollback()


    def do_respond_to_post(self, arg):
        post_id = input("Input post id: ")
        response = input("Input response: ")

        if not (post_id and response):
            print("Missing input. Respond to post failed.")
        
        try:
            find_post_query = "select * from Post where postID = {};".format(post_id)
            result = self.client.executeQuery(find_post_query).fetchall()

            if not result:
                print("Post not found")
            else:
                create_respond_post = "insert into Post (userID, text) values (%s, %s);"
                params = (self.current_userID, response)

                respond_post_id = self.client.executeQuery(create_respond_post, params).lastrowid

                respond_query = "insert into Respond_Post values (%s, %s);"
                params = (post_id, respond_post_id)

                self.client.executeQuery(respond_query, params)
                self.client.commit()
                print("You have responded to post {} successfully.".format(post_id))
        except mysql.connector.Error as error :
            print("Respond to post failed with error: {}".format(error))
            self.client.rollback()


    def do_get_new_posts(self, arg):
        try:
            # Get the new post from the followed topic and followed user
            get_new_post_query = '''
                SELECT postID,
                    userID,
                    postTitle,
                    text,
                    createTime,
                    thumbsUp,
                    thumbsDown
                FROM Post
                INNER JOIN Post_Topic USING (postID)
                INNER JOIN Topic USING (topicID)
                WHERE (topicID IN
                        (SELECT topicID
                        FROM Subscribe_Topic
                        WHERE userID = {} )
                    OR userID IN
                        (SELECT userID
                        FROM Subscribe_Topic
                        WHERE followerID = {} ))
                AND (postID NOT IN
                        (SELECT postID
                        FROM Read_Post
                        WHERE userID = {} ));
            '''.format(self.current_userID, self.current_userID, self.current_userID)
            
            result = self.client.executeQuery(get_new_post_query).fetchall()

            if not result:
                print("There is no new post. You are up to date!")
            else:
                df = pd.DataFrame(result, columns=[
                    'postID',
                    'userID',
                    'postTitle',
                    'text',
                    'createTime',
                    'thumbsUp',
                    'thumbsDown'
                ])
                print(df)

                # Record read posts
                read_posts = [(read_post[0], self.current_userID) for read_post in result]
                insert_read_post_query = "insert into Read_Post values (%s, %s);"

                self.client.cursor.executemany(insert_read_post_query, read_posts)
                self.client.commit()
                print("Get new post successfully.")
        except mysql.connector.Error as error :
            print("Get new posts failed with error: {}".format(error))
            self.client.rollback()


    def do_get_all_posts(self, arg):
        try:
            # Get the new post from the followed topic and followed user
            get_all_post_query = '''
                SELECT postID,
                    userID,
                    postTitle,
                    text,
                    createTime,
                    thumbsUp,
                    thumbsDown
                FROM Post
                INNER JOIN Post_Topic USING (postID)
                INNER JOIN Topic USING (topicID)
                WHERE (topicID IN
                        (SELECT topicID
                        FROM Subscribe_Topic
                        WHERE userID = {} )
                    OR userID IN
                        (SELECT userID
                        FROM Subscribe_Topic
                        WHERE followerID = {} ));
            '''.format(self.current_userID, self.current_userID, self.current_userID)
            
            result = self.client.executeQuery(get_all_post_query).fetchall()

            df = pd.DataFrame(result, columns=[
                'postID',
                'userID',
                'postTitle',
                'text',
                'createTime',
                'thumbsUp',
                'thumbsDown'
            ])
            print(df)
        except mysql.connector.Error as error :
            print("Get all posts failed with error: {}".format(error))
            self.client.rollback()


    def do_get_my_posts(self, arg):
        try:
            get_my_posts_query = "select * from Post where userID = {};".format(self.current_userID)

            result = self.client.executeQuery(get_my_posts_query).fetchall()
            if not result:
                print("Empty posts.")
            else:
                my_posts = pd.DataFrame(result, columns=[
                    'postID',
                    'userID',
                    'text',
                    'createTime',
                    'thumbsUp',
                    'thumbsDown'
                ])
                print(my_posts)
        except mysql.connector.Error as error :
            print("Get my posts failed with error: {}".format(error))
            self.client.rollback() 


if __name__ == '__main__':
    SocialNetworkClient().cmdloop() 
	
