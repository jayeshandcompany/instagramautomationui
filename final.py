from instagrapi import Client
# import credentials
import time
import random
import colorama

import validators
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd

import io

colorama.init(autoreset=True)
commen = ['Nice shot! ',
          'I love your profile! 😊 ',
          'Your feed is an inspiration 👍',
          'Just incredible 😮',
          'What camera did you use 📸 ',
          'Love your posts 🤗',
          'Looks awesome 👌',
          'Getting inspired by you 👏',
          '🙋‍ Yes!',
          'I can feel your passion 💪',
          'Awesome 👌',
          'Wow!😮']


st.set_page_config(
    page_title="Instagram Bot",
    page_icon="instagram",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

if "page" not in st.session_state:
    st.session_state.reload=False
    st.session_state.client = Client()
    st.session_state.username = ""
    st.session_state.pwd = ""
    st.session_state.loc=False
    st.session_state.loc2=False
    st.session_state.loc3=False
    st.session_state.a=None
    st.session_state.medias=None
    st.session_state.limit=False

    st.session_state.run=0
    st.session_state.r=0
    st.session_state.logged=False

    st.session_state.page = 0
    st.session_state.msg=False
    st.session_state.copy1=False
    st.session_state.copy2=False
    st.session_state.hash=False
    st.session_state.hash2=False
    st.session_state.follow=True
    st.session_state.dife=None
    st.session_state.diff2=None

def reset(i):
    if i==1:
        st.session_state.run = 0
        st.session_state.logged = False
        st.session_state.page = 0
        st.session_state.reload = False
        st.session_state.client = Client()
        st.session_state.username = ""
        st.session_state.pwd = ""
        st.session_state.r = 0

    st.session_state.diff2 = None
    st.session_state.msg = False
    st.session_state.copy1 = False
    st.session_state.copy2 = False
    st.session_state.hash = False
    st.session_state.hash2 = False
    st.session_state.follow = True
    st.session_state.dife = None
    st.session_state.loc = False
    st.session_state.loc2 = False
    st.session_state.loc3 = False
    st.session_state.a = None
    st.session_state.medias = None
    st.session_state.limit = False
placeholder = st.empty()
def nextpage(): st.session_state.page += 1
def restart(): st.session_state.page = 0






















if st.session_state.reload==False:

    with placeholder.container():
        st.markdown("<h1><center> INSTAGRAM - BOT</h1> ",unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)

        c2.image("logo.png", width=150)

        e = st.text("Establishing Secured Connection ")
        with st.spinner('Please Wait '):

            time.sleep(5)
        e.empty()

if st.session_state.page==0:
    with placeholder.container():
        st.markdown("<h1><center> INSTAGRAM - BOT</h1> ",unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)

        c2.image("logo.png", width=150)
        with st.form("my"):


                if st.session_state==False:

                    success=st.success( "Succesfully Established !")
                    time.sleep(3)
                    success.empty()
                st.session_state.reload=True
                st.markdown("<h2><center>Login</h2>",unsafe_allow_html=True)
                a=st.warning( " Please Turn off your Two Factor Authentication Before Login ")

                st.session_state.username = st.text_input("Enter Instagram username : ")
                st.session_state.pwd=st.text_input("Enter Password : ",type="password")
                c1,c2,c3=st.columns(3)
                with c2:
                    login = st.form_submit_button("Login")
                if login:
                    logged=False
                    st.session_state.run=1
                    a.empty()
                    st.session_state.page+=1








if st.session_state.page!=0:


        with st.spinner("Trying To log in"):

            try:
                username=st.session_state.username


                if st.session_state.run==1 and st.session_state.logged==False:

                    st.session_state.client.login(username, st.session_state.pwd)
                    st.session_state.page+=1





            except Exception as e:
                e1 = str(e)
                a = e1.split(" ")
                st.session_state.run=0
                st.session_state.page = 0
                st.error(f"{e}")

        if st.session_state.page==2:
            if st.session_state.logged==False:
                with placeholder.container():
                    st.success(f"Succesfully logged in!! ^_^ as {st.session_state.username}")
                    st.balloons()

                    a = st.warning(" Please don't use The Bot Repeatedly Over a Short period of time ")
                    with st.spinner("please wait Loading Bot O_o"):
                        time.sleep(random.randint(2, 7))
                        a.empty()
                st.session_state.logged=True
            client=st.session_state.client

            with placeholder.container():
                with st.sidebar:


                        choose = option_menu("Instagram Bot",
                                             ["About", "Follow Back", "Location", "Hashtag", "Message", "Unfollow",
                                              "Copy",
                                              "Like", "Logout"],
                                             icons=['robot', 'person-badge', 'geo-alt-fill', 'hash', 'chat-dots-fill',
                                                    'person-dash', 'clipboard-check', 'star-fill', 'box-arrow-in-left'],
                                             menu_icon="instagram", default_index=0,
                                             styles={
                                                 "container": {"padding": "5!important", "background-color": "#fafafa"},
                                                 "icon": {"color": "black", "font-size": "25px"},
                                                 "nav-link": {"font-size": "16px", "text-align": "left",
                                                              "margin": "0px",
                                                              "--hover-color": "#eee"},
                                                 "nav-link-selected": {"background-color": "#FF6F61"},
                                             }
                                             )


                        if choose == "About":
                            reset(0)
                            with placeholder.container():
                                st.title("INSTAGRAM -BOT")

                                st.header("Welcome to our Instagram bot!")
                                st.markdown("<h5>1)The <b><u>Follow Back</u></b> feature of an Instagram bot  follow other Instagram accounts that have followed your account.</h5>",unsafe_allow_html=True)
                                st.markdown("<h5>2)The <b><u>Location</u></b> feature of an Instagram bot allows users to automatically like posts that are tagged with a specific location or within a certain geographic area.</h5>",unsafe_allow_html=True)
                                st.markdown("<h5>3)The <b><u>Hashtag</u></b> feature of an Instagram bot allows users to automatically like posts that include specific hashtags</h5>",unsafe_allow_html=True)
                                st.markdown("<h5>4)The <b><u>Message</u></b> feature of an Instagram bot allows users to send the same message to multiple Instagram accounts simultaneously</h5>",unsafe_allow_html=True)
                                st.markdown("<h5>5)The <b><u>Unfollow</u></b> feature of an Instagram bot allows users to automatically unfollow accounts that they have previously followed</h5>",unsafe_allow_html=True)
                                st.markdown("<h5>The <b><u> Copy </u></b> feature is a customized Features that allows users to automatically follow someone's followers or followings</h5>", unsafe_allow_html=True)
                                st.markdown("<h5>7)The <b><u>Like</u></b> feature of an Instagram bot allows users to automatically like posts on Instagram</h5>",unsafe_allow_html=True)
                                st.markdown("<h5>8)The <b><u>Logout</u></b> feature of an Instagram bot allows users to log out of their Instagram account from the bot.</h5>",unsafe_allow_html=True)




                        elif choose == "Follow Back":

                            def follow():
                                print(st.session_state.follow)






                                with placeholder.container():

                                    if st.session_state.follow:
                                        print("aaya")
                                        with st.spinner("FETCHING RECENT FOLLOWERS"):

                                            user_id = client.user_id_from_username(st.session_state.username)
                                            followers = client.user_followers(str(user_id))
                                            following = client.user_following(str(user_id))



                                            st.session_state.dife = {k: v for k, v in followers.items() if k not in following}
                                            res = not bool(st.session_state.dife)
                                            if res == True:
                                                st.success("No Recent Followers found !")
                                                return
                                            # print(diff)

                                    with placeholder.container():
                                        st.success("Succesfully fetched")



                                st.session_state.follow=False
                                print("ye")


                                with placeholder.container():
                                    if st.session_state.r==2:
                                        st.success(" Already Followed All Followers please login again to refresh!")
                                        return


                                    st.success(" new Followers Found Do you want To follow them ")
                                    if st.button('Yes'):
                                        st.session_state.r += 1
                                        a = None
                                        with placeholder.container():
                                            with st.spinner("Trying To  follow Recent users !...."):

                                                for i, media in enumerate(st.session_state.dife):
                                                    # print(media)
                                                    data = st.session_state.dife[media]
                                                    # print(data)
                                                    # print(type(data))

                                                    if data.is_private == True:

                                                        a = st.write(
                                                            f"Trying to Follow (Private) user: {data.username} ")
                                                        time.sleep(random.randint(1, 4))

                                                    else:
                                                        a = st.write(
                                                            f"Trying to Follow (Public) user: {data.username} ")
                                                        time.sleep(random.randint(1, 4))

                                                    st.session_state.client.user_follow(data.pk)

                                                    b = st.write(f"Succesfully Followed user: {data.username} ")
                                            st.success("Succesfully Followed all recent followers ^_^")
                                            st.session_state.follow=None

                                # with open('file.txt', 'w') as file:
                                #     file.write(pickle.dumps(diff))
                                # with open('finally.txt', 'w+',encoding="utf-8") as file:
                                #     file.write(str(diff))

                            follow()


                        elif choose == "Unfollow":
                            def unfollow():
                                with placeholder.container():


                                    try:
                                        ch = st.selectbox("Please Select whom do you want to unfollow",('all non-followers','all followers' ))
                                    except:
                                        print("Sorry you have selected wrong input please try again")
                                    a = 1
                                    if st.button('Confirm'):
                                        if ch == "all followers":
                                            with st.spinner("Please wait Fetching Followers!"):
                                                followers = st.session_state.client.user_followers(st.session_state.client.user_id)

                                                res = not bool(followers)
                                                if res == True:
                                                    st.success( "No Followers found ")
                                                    return


                                            st.success( "Successfully Fetched!")
                                            # if res == True:
                                            #     print(Fore.LIGHTRED_EX+"No non followers found ")
                                            #     return 1
                                            for user_id in followers.keys():
                                                if a == 6:
                                                    st.error( "Please Don't Unfollow more than 5 followers at same time \nPlease Try again Later !")

                                                user = st.session_state.client.username_from_user_id(user_id)
                                                st.write( f"Unfollowing user : {user}")
                                                a += 1
                                                time.sleep(random.randint(1, 3))

                                                try:
                                                    st.session_state.client.user_unfollow(user_id)
                                                except:
                                                    continue
                                                st.success( f"Successfully Unfollowed! {user}")

                                        elif ch == "all non-followers":
                                            with st.spinner( "Please wait Fetching non Followers!"):
                                                followers = st.session_state.client.user_followers(st.session_state.client.user_id)
                                                following = st.session_state.client.user_following(st.session_state.client.user_id)
                                                diff = {k: v for k, v in following.items() if k not in followers}
                                            res = not bool(diff)
                                            if res == True:
                                                st.success( "No non followers found ")
                                                return


                                            for i, media in enumerate(diff):
                                                if a == 6:
                                                    st.error( "Please Don't Unfollow more than 5 followers at same time \nPlease Try again Later !")
                                                    return 1
                                                # print(media)
                                                data = diff[media]
                                                # print(data)
                                                # print(type(data))

                                                st.write( f"Trying to Unfollow user: {data.username} ")

                                                time.sleep(random.randint(2, 5))
                                                st.session_state.client.user_unfollow(data.pk)
                                                a += 1

                                                st.success( f"Succesfully Unfollowed user: {data.username} ")
                                            st.success("Succesfully Unfollowed all non followers ^_^")
                                        else:
                                            print( "Sorry you have selected wrong input\nplease try again")
                                            return 1
                            unfollow()

                        elif choose == "Location":
                            def searchLocation():
                                with placeholder.container():
                                    lo = st.number_input( "please enter the longitude",key='x')
                                    la = st.number_input("please enter the latitude",key='y')
                                    c1,c2,c3=st.columns(3)
                                    first=None
                                    with c2:
                                            first=st.button('Confirm',key="fssf",disabled=st.session_state.loc)
                                    if first or st.session_state.loc:

                                        a = None
                                    # print(a)
                                        if st.session_state.loc==False:

                                            st.session_state.loc = True
                                            if st.session_state.loc2==False:
                                                with st.spinner( "Fetching Location!"):
                                                    try:
                                                        location = st.session_state.client.location_search(lo, la)[0]
                                                        location1 = st.session_state.client.location_complete(location)
                                                        st.session_state.a = location1.dict()
                                                    except:
                                                        st.error( "No location found for this cordintes \nplease try again with new cordinates ")
                                                        return 1
                                        a=st.session_state.a
                                        with placeholder.container():
                                            st.success(f"Successfully Fetched! Location: {a['name']}")
                                            c = st.slider(f"ammount of post you want to fetch for location : ",min_value=1,max_value=10,step=1)

                                            if st.button('Confirm',disabled=st.session_state.loc2)or st.session_state.loc2:
                                                res=True


                                                st.session_state.loc2 = True
                                                medias=st.session_state.medias
                                                if st.session_state.loc3==False:
                                                    with st.spinner(f"Fetching Top Posts in location :  {a['name']}"):

                                                        st.session_state.medias = st.session_state.client.location_medias_top(a['pk'], amount=c)
                                                    res = not bool(st.session_state.medias)
                                                    if res == True:
                                                        st.error(f"Unfortunately no post found for {a['name']}")
                                                        return True

                                                with placeholder.container():
                                                    st.success( "Successfully Fetched")
                                                    st.session_state.loc3 = True
                                                    placeholder.container().empty()
                                                    cc = st.selectbox("Do you want to Comment on posts? it can help you increase reach!",( 'No','Yes'))
                                                    if st.button('Confirm',key="final") :

                                                        comen = random.randint(2, 6)
                                                        with st.spinner("Please wait"):
                                                            for i, media in enumerate(medias):
                                                                u = media.user.username
                                                                if i % comen == 0:
                                                                    if cc == "Yes":
                                                                        if media.has_liked == True:
                                                                            continue
                                                                        r = random.choice(commen)
                                                                        r1 = r + " @" + u
                                                                        try:
                                                                            st.session_state.client.media_comment(media.id, r1)
                                                                        except:
                                                                            continue
                                                                        st.success(f"Commented {r} under loc: {a['name']} Posted By @{u}")
                                                                try:
                                                                    st.session_state.client.media_like(media.id)
                                                                except:
                                                                    time.sleep(random.randint(1, 5))
                                                                    continue

                                                                st.success( f"Liked post number {i + 1} of location: {a['name']} Posted By  @{u}")
                                                                time.sleep(random.randint(1, 5))

                                                            return 1


                            loc = searchLocation()
                        elif choose == "Message":
                            def sendMessage():
                                with placeholder.container():

                                    ch = st.selectbox("whom do you want to  send bulk messages ",('all following' ,'all followers'))
                                    if st.button('Confirm') or st.session_state.msg:
                                        st.session_state.msg=True


                                        m = st.text_input("Please Enter the message that you want to send : ")
                                        if st.button('Confirm',key="sfff"):


                                            ab = 1
                                            # print(diff)
                                            if ch == 'all followers':
                                                with st.spinner("Please wait Fetching Followers!"):
                                                    followers = client.user_followers(client.user_id)
                                                res = not bool(followers)
                                                if res == True:
                                                    st.error("No Followers found ")
                                                    return True
                                                with st.spinner("Please wait sending Messages"):
                                                    for user_id in followers.keys():
                                                        if ab % 5 == 0:
                                                            st.session_state.limit=True
                                                            cho = st.selectbox("Do You want to stop sending Messages ",('Yes','No'))
                                                            if st.button('Confirm',key="fi"):
                                                                if cho =="Yes":
                                                                    return 1
                                                                else:
                                                                    st.session_state.limit=False

                                                            if st.session_state.limit==False:
                                                                user = client.username_from_user_id(user_id)
                                                                st.write(f"Messaging user : {user}")
                                                                time.sleep(random.randint(1, 3))
                                                                try:
                                                                    client.direct_send(text=m, user_ids=[user_id])
                                                                except:
                                                                    continue
                                                                st.success( f"Succesfully messaged user: {user} ")
                                                                ab += 1

                                                        st.success( "Successfully Message send to all followers!")
                                                        return 1

                                            elif ch == 'all following':
                                                following = client.user_following(client.user_id)

                                                res = not bool(following)

                                                if res == True:
                                                    st.error( "No following found ")
                                                    return 1
                                                ab = 1
                                                with st.spinner("Please wait sending Messages"):
                                                    for user_id in following.keys():
                                                        if ab % 5 == 0:
                                                            cho = st.selectbox("Do You want to stop sending Messages ",
                                                                               ('Yes', 'No'))
                                                            if st.button('Confirm', key="fi"):
                                                                if cho == "Yes":
                                                                    return 1
                                                                else:
                                                                    st.session_state.limit = False

                                                        if st.session_state.limit == False:
                                                            user = client.username_from_user_id(user_id)
                                                            st.write(f"Messaging user : {user}")
                                                            time.sleep(random.randint(1, 3))
                                                            try:
                                                                client.direct_send(text=m, user_ids=[user_id])
                                                            except:
                                                                continue

                                                            st.success( f"Succesfully messaged user: {user} ")
                                                            ab += 1
                                                    st.success( "Succesfully messaged all following ^_^")
                                                    return 1


                            sm = sendMessage()
                        elif choose == "Hashtag":
                            def hashTag():
                                with placeholder.container():
                                    h = st.text_input("Please enter your Hashtag sep by (#) : ")
                                    if st.button('Confirm')or st.session_state.hash:
                                        st.session_state.hash=True
                                        if st.session_state.hash2==False:
                                            hashtag1 = h.split("#")
                                            hashtag = hashtag1[1:]
                                            # print(hashtag)
                                            a = st.slider("Please enter the number of post that you want to fetch for  each # : ",min_value=1,max_value=20,step=1)

                                            cc = st.selectbox( "Do you want to Comment on posts? it can help you increase reach!",( 'yes','No'))
                                            if st.button('Confirm',key='fil') or st.session_state.hash2:
                                                comen = random.randint(2, 6)
                                                for has in hashtag:
                                                    with st.spinner(f"please Wait Fetching  Posts For #{has}"):
                                                        medias = client.hashtag_medias_recent(has.lower(), a)
                                                        res = not bool(medias)
                                                        if res == True:
                                                            st.error( f"Unfortunately no post found for #{has}")
                                                            continue
                                                    st.success(f"Successfully Fetched Posts for #{has}")
                                                    # medias.append(m)
                                                    for i, media in enumerate(medias):
                                                        u = media.user.username
                                                        # print(media)
                                                        if i % comen == 0:
                                                            if cc == "Yes":
                                                                if media.has_liked == True:
                                                                    continue
                                                                r = random.choice(commen)
                                                                r1 = r + " @" + u
                                                                try:
                                                                    client.media_comment(media.id, r1)
                                                                except:
                                                                    continue
                                                                st.success( f"Commented {r} under #{has} Posted By {u}")
                                                        try:
                                                            client.media_like(media.id)
                                                        except:
                                                            time.sleep(random.randint(1, 5))
                                                            continue
                                                        st.success(f"Liked post number {i + 1}  under #{has} Posted By {u}")
                                                        time.sleep(random.randint(1, 5))
                            hashTag()

                        elif choose == "Copy":
                            def copy():
                                with placeholder.container():

                                    a = st.text_input("Please Enter the Username or the link of the profile Whose Followers/Following You want  to copy : ")
                                    if st.button('Confirm',disabled=st.session_state.copy1) or st.session_state.copy1:
                                        st.session_state.copy1=True
                                        if st.session_state.copy2==False:
                                            valid = validators.url(a)
                                            with st.spinner( "Please Wait Fetching Data From Link/Username"):
                                                if valid == True:
                                                    try:
                                                        link1 = a.split("?")
                                                        # print(link1)
                                                        a = link1[0]
                                                    except:
                                                        pass
                                                    link = a.split("m/")[1]
                                                    if link[-1] == "/":
                                                        username = link[:-1]

                                                else:
                                                    if a[0] == "@":
                                                        username = a[1:]
                                                try:
                                                    user_id = client.user_id_from_username(username)
                                                    st.success(f"Account  Successfully Found For username :@{username}")
                                                except:
                                                    st.error("Unfortunately No account Found For Username : ", username)
                                                    return

                                        a = st.selectbox("What do you need to  Copy",('Followers','Following'))
                                        if st.button('Confirm',key="sff"):

                                            if a == 'Followers':
                                                with st.spinner( f"Please Wait Fetching Followers of @{username}"):
                                                    st.session_state.list11 = client.user_followers(user_id)
                                                    time.sleep(2)

                                            if a == 'Following':
                                                with st.spinner(f"Please Wait Fetching Followings of @{username}"):
                                                    st.session_state.list11 = client.user_following(user_id)
                                                    time.sleep(2)

                                            runned = 0


                                            st.success( "SuccessFully Fetched !")

                                            with st.spinner("Please wait Tring To folloq"):
                                                for i, media in enumerate(st.session_state.list11):
                                                    # print(media)
                                                    data = st.session_state.list11[media]
                                                    # print(data)
                                                    # print(type(data))
                                                    if runned == 10:
                                                        st.error( "Please Don't follow more than 10 followers at same time \nPlease Try again Later !")
                                                        return 1

                                                    if data.is_private == True:

                                                        st.write(f"Trying to Follow (Private) user: {data.username} ")
                                                    else:
                                                        st.write(f"Trying to Follow (Public) user: {data.username} ")

                                                    time.sleep(1.5)
                                                    client.user_follow(data.pk)
                                                    runned += 1
                                                    st.success( f"Succesfully Followed user: {data.username} ")
                            copy()

                        elif choose == "Like":
                            def like():
                                with placeholder.container():
                                        ch=st.selectbox("Please select Group whose Posts do you wanna like ",('all Messengers','all Followers','all Following'))
                                        if st.button('Confirm'):



                                            liked = 1
                                            if ch == 'all Messengers':
                                                with st.spinner( "Please Wait Fetching Users "):
                                                    di1 = client.direct_pending_inbox()
                                                    di2 = client.direct_threads()
                                                    di = di1 + di2
                                                    # print("di=",di)
                                                    dm = []
                                                st.success("Successfully Fetched !")

                                                for i, user in enumerate(di):
                                                    a = user.messages
                                                    for i, b in enumerate(a):
                                                        if i == 1:
                                                            break
                                                        dm.append(b.user_id)
                                                for user_code in dm:

                                                    name = client.username_from_user_id(user_code)
                                                    try:
                                                        medias = client.user_medias(user_code)
                                                    except:
                                                        st.error( f"@{name}  is having Private account Moving To next one!")
                                                        continue
                                                    # print(medias)
                                                    for i, media in enumerate(medias):
                                                        # u = media.user.username
                                                        if i == 5:
                                                            st.success( f"SuccessFully Liked  5 post of @{name} Moving To another Now ")
                                                            break
                                                        try:
                                                            client.media_like(media.id)
                                                        except:
                                                            continue
                                                        st.success( f"Successfully Liked Post {i + 1} of @{name}")
                                                        time.sleep(random.randint(1, 5))

                                                    # print(Fore.LIGHTGREEN_EX+f"Successfully Liked all Posts of @{name}")
                                            diff=None
                                            if ch == 'all Followers':
                                                with st.spinner("Please Wait Feching Followers !"):
                                                    diff = client.user_followers(client.user_id)
                                                    time.sleep(2)
                                            if ch == 'all Following':
                                                with st.spinner("Please Wait Feching Following !"):
                                                    diff = client.user_following(client.user_id)
                                            with st.spinner("Please wait Liking Posts"):
                                                for i, media in enumerate(diff):
                                                    # print(media)
                                                    data = diff[media]
                                                    name = data.username
                                                    user_code = client.user_id_from_username(name)

                                                    try:

                                                        medias = client.user_medias(user_code)
                                                    except:
                                                        st.error( f"@{name}  is having Private account Moving To next one!")
                                                        continue
                                                    # print(medias)
                                                    for i, media in enumerate(medias):
                                                        # u = media.user.username
                                                        # print(media)
                                                        if i == 5:
                                                            st.success( f"SuccessFully Liked  5 post of @{name} Moving To another Now ")
                                                            break
                                                        try:
                                                            client.media_like(media.id)
                                                        except:
                                                            continue
                                                        st.success( f"Successfully Liked Post {i + 1} of @{name}")
                                                        time.sleep(random.randint(1, 5))

                                    # print(Fore.LIGHTGREEN_EX+f"Successfully Liked all Posts of @{name}")
                            like()

                        elif choose == "Logout":
                            st.session_state.client.logout()
                            reset(1)



    # client.user_medias()





