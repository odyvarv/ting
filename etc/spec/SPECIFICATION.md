# Ting

June 15, 2015 - August 25, 2015

dionyziz for the Ting team.

Ting is a chat platform. It runs on ting.gr. This document specifies how it works.

# Workflow
People on ting exchange messages. Messages can be exchanged either in channels
(known as "tings"), or privately. Channels are public and can be looked at by
anyone, where they can see the messages exchanged. Privates are messages
exchanged directly between two people and can only be viewed by these people.
Channels and privates are collectively referred to as conversations.

Ting is a website that works both on desktop and on mobile.

Ting consists of serveral screens:

* The login screen
* The chat screen
* The settings screen

These are described below. When the user enters the URL ting.gr on their
browser, they are taken to the Login screen. If they enter www.ting.gr, they
are redirected to ting.gr and appropriate URL parameters are appended.

When the user enters the URL ting.gr/channel, where channel is any
valid channel name, the user is taken to the Login screen with the active
conversation set to the channel specified in the URL. When the user enters
the URL ting.gr/u/user, where user is any valid user name, the user is taken
to the Login screen with the active conversation set to a private with the
user specified.

However, if the user has stored credentials, then the Login screen is skipped
and the user is taken directly to the Chat screen.

The active conversation remains until the web page is refreshed, a different
URL is visited, or the active channel is manually changed. When the active
conversation is changed, the URL is changed to reflect that.

Once a user enters ting, they can then see who is online on the platform among
the recent people they had a conversation with.

The users can exchange messages in multiple channels. Messages exchanged are
per-channel. Each message sent to a channel is delivered only to the selected
channel.

Message history is stored in a per-conversation basis. When a user makes a
conversation active, they are shown some of the messages history.

# Channels
If no conversation is specified in the URL, the default channel name is used,
which is the channel name "ting". Channel names are validated as follows upon
visiting a ting URL:

1. The channel name is at least 1 character and at most 20.
2. The channel name must consist of only the following characters:
 - The lower-case and upper-case latin characters a-z and A-Z.
 - The numbers 0-9.
 - The symbols _ . -

If an invalid channel is specified, the user is redirected to the default
channel and the URL shown is ting.gr without a channel name. The same applies
if an invalid username is specified.

There is no notion of creating or destroying a channel. A channel exists purely
because of the messages exchanged within it.

# UX foundation
The UX is in Greek. The text towards the user will be informal. Singular
form is used for everything. Informal words are preferred over formal words.
For example, the word "πληκτρολόγησε" should be replaced by "γράψε". The goal
is to make the user feel at ease, relaxed, and in a friendly environment.

# Target audience
The target audience for Ting is teenagers from Greece aged 12 - 21 years old.
The purpose of the chat is to bring people close together and allow strangers
who live in the same country and are of similar age to get to know each other.
We should make it a point in the UX to avoid the purpose of many other chat
rooms which is romantic or sexual interest, and focus on directing the user to
make friendly, public conversations.

# Login screen
The Ting login system is somewhat peculiar in that it does not involve any
passwords. This is for usability purposes. Ting users are authenticated by
having their machine remember their credentials when they register and when
they login. Registering is done by entering only a username.

If a user wants to keep their username, they only have to enter an e-mail
address. This e-mail address is later used to recover their account if they
have wiped their login credentials.

The Login screen consists of only a modal window with the heading "Ting", a
textbox and a button.

![Login screen](http://i.imgur.com/FKcFIzW.jpg)
*Image: The login screen*

The placeholder text in the textbox is "Γράψε ένα ψευδώνυμο". The textbox is
focused by default when the screen is visited. The placeholder text is hidden
when the user starts typing some text, unless the text is cleared. Pressing the
Enter key when the keyboard is focused on the textbox is equivalent to pressing
the button.

The button has the text "Μπες". Upon clicking the button, the username entered
is verified as follows:

1. The username is at least 1 character and at most 20.
2. The username must consist of only the following characters:
 - The lower-case and upper-case latin characters a-z and A-Z.
 - The lower-case and upper-case greek characters α-ω and Α-Ω.
 - The numbers 0-9.
 - The symbols . , / ? ~ ! @ # $ % ^ & * ( ) - _ = + [ ] { } \ | ' " ` ; :
3. The username must not be reserved.

All usernames are not reserved by default. If the username is valid, the
username is reserved and the user is taken to the Chat screen. The username is
then associated with that user. The user's credentials are then stored on the
machine they used to login. The next time the user accesses ting, the
credentials are used to skip the Login screen. Once a username becomes
reserved, no other user is allowed to use it, even if the user is not currently
online.

If the username is invalid, the textbox border is changed to red, the
content text color is changed to red and an appropriate error is displayed as
follows:

1. If the username field is empty, the error message is "Γράψε ένα ψευδώνυμο."
2. If the username field is too large, the error message is "Το ψευδώνυμο
   πρέπει να είναι έως 20 γράμματα."
3. If the username field contains forbidden characters, the error message is
   "Το ψευδώνυμο πρέπει να περιλαμβάνει μόνο γράμματα, αριθμούς ή σύμβολα."
4. If the username is reserved, the error message is "Το ψευδώνυμο
   το έχει άλλος. [Εγώ είμαι]"

The error message is displayed above the textbox.

The "[Εγώ είμαι]" button is displayed only if the username entered has an
associated e-mail address with it. It is displayed on a separate line and can
be used for the user to claim a previously registered username. Clicking this
button changes the whole login window contents to the following text:

"Σου στείλαμε ένα e-mail. Πάτησε το σύνδεσμο για να μπεις ως [nickname]."

Where "[nickname]" is the nickname the user used to login. In addition, an
e-mail is sent to the e-mail address associated with the user. The e-mail
address reads as follows:

"Γεια σου [nickname].

Μπορείς να μπεις στο ting πατώντας τον παρακάτω σύνδεσμο:

[link]"

Where "[nickname]" is the nickname of the user and "[link]" is a link the user
can use to login to their account. When the link is clicked by the user, they
are taken to Ting, to the channel they had entered previously when they tried
to access ting. They are taken directly to the Chat screen and their
credentials are stored.

These e-mail links can be used within 24 hours and they expire afterwards. If
an expired link is clicked, then the Ting application opens and displays only a
single error message with the following text:

"Ο σύνδεσμος που πάτησες έληξε. [Θέλεις έναν καινούργιο;]"

Clicking the button sends a new email to the user with a new link for logging
in. The intended channel is maintained in this link also.

On mobile, the whole screen is used to display the login window.

![Mobile login screen](http://i.imgur.com/nUfvfVz.jpg)
*Image: The mobile login screen*

On mobile, care should be taken to ensure the button is visible while the
username is being entered.

# Chat screen
The chat screen consists of the following elements:

1. A top bar
2. A recent conversations list
3. A chat history
4. A message area

![Chat screen](http://i.imgur.com/4kl8upL.jpg)
*Image: The chat screen*

The top bar is located at the top and takes up the whole screen horizontally.
On the top left, it has the text "ting". On the right, it has a cog icon.
Clicking the cog icon pops up a menu with two options: Settings and Log out.
Clicking on Settings takes the user to the Settings screen. Clicking Log out
logs the user out and wipes their user credentials from their machine. If the
user has no e-mail address associated with their account, then Log out also
frees up the username for future use. Otherwise, the username remains reserved.
After logging out, the Ting application is replaced with the following text:

"Τα ξαναλέμε σύντομα! [Πίσω στο ting]"

Clicking the button takes the user back to the Ting application and allows them
to start over with logging in anew.

On mobile, there is no top bar.

Below it, the screen is split in two areas vertically. The left area contains
the recent list and the right area is split horizontally in two smaller areas.
The top portion is the larger and is the chat history. The bottom portion is
the message area. The portions are not resizable. If the active conversation is
a private message, there is an additional area above the message area, the user
information area.

The recent list contains a list of recently used channels and recently accessed
private message partners. Recent conversations are shown from most recent to
least recent, one below the other. There is one currently active conversation
at a time. That conversation is shown at the top of the recent conversation
list. Recent conversations that are channels simply display the channel name.
Recent conversations that are privates display the person's avatar, their name,
and their online status. The online status is displayed with a green dot on the
right of their name in case they are online.

If the list of conversations is too long to fit, a vertical scrollbar is
displayed on the right-hand side of the nick list.

At the top of the recent conversations list is a searchbox. The searchbox
allows the user to type in order to filter items from the recent conversation
list. When no text is entered in the search box, the text box has the
placeholder text "Βρες ανθρώπους ή tings". As soon as the user starts typing,
the placeholder text disappears unless they clear their text. While there is
text in the search textbox, an "X" is shown at the right of the textbox, which
allows the user to clear their search text. While typing, the recent
conversations list is filtered by the search text through a prefix-match test.

The currently active conversation is shown highlighted at the top of the recent
conversation list. Recent conversations are reordered only by reactivating
them: They are not reordered by receiving messages in them or sending messages
in them.

Conversations with unread messages are also highlighted, but in a different
color. Unread messages are any messages of user-interest which have not been
viewed by the user yet. Activating a conversation with unread messages marks
their messages as read. Messages of user-interest are defined as any received
message in a private conversation, or any message mentioning the user's name in
a channel.

If there are unread messages in the active conversation when the user is not
active (has switched to another tab or window), the window title gets prepended
with the count of unread messages in parentheses. When the user is active
again, the count is removed from the title and the previously unread messages
are marked as read.

The message history contains a list of messages posted by everyone in the
active conversation. The messages are displayed in chronological order from top
to bottom. When the user enters a conversation, the message history consists of
the most recent 100 messages exchanged by the users priorly and is stored on
the server.

Each message posted has the following form: "[avatar] [username] Message",
where username contains the username of the person making the post and Message
contains the text posted. The message is displayed in a comicbook-like bubble
indicating that someone is speaking. Messages of user-interest in channels are
highlighted. Messages sent and received are displayed in different style.

If a text is too long to fit in one line, it is wrapped around to the next
line. No horizontal scrollbar is ever displayed in the history area.

If there are less messages than the chat history can fit, the messages are
displayed at the bottom of the chat history area. Otherwise, a vertical
scrollbar is shown.

Every time a message is posted by someone, a new chat message is appended to
the bottom of the chat history area, and the area is scrolled towards the
bottom to make the new message visible. This happens unless the user has
scrolled upwards into the history enough to read older messages. In that case,
a new message being posted does not affect the scrolling position of the
history area.

For efficiency reasons, very old messages can be removed from the chat history.

The user information area is shown above the message history area in case the
currently active conversation is a private. The user information area shows the
partner's avatar and username.

The message area is a textbox. The textbox is focused by default when the user
enters the Chat screen. The textbox has the placeholder "Γράψε ένα μήνυμα...".
When the user starts typing some text, the placeholder is hidden, unless the
text the user entered is deleted, in which case the placeholder text reappears.
If a user enters a long message, the text is wrapped within the textbox.
Horizontal scrollbars never appear in the message area.

When a user enters a non-empty message and presses the Enter key, the message
is sent. There is no separate button to send a chat. When a message is sent by
a user, it is delivered to everyone else who is currently online in the chat in
the active channel. The textbox in the message area is then cleared, but
remains focused. The message appears immediately on the side of the sending
party.

On mobile, the chat screen is separated into two different screens. These are
the recent conversations screen and the mobile chat screen. The semantics are
similar to the above desktop version, with the mobile differences described
below.

In the recent conversations screen, the text "Ting" is displayed at the top.
Next to it, on the right, is a cog icon. Clicking the cog icon displays a
pop-up menu with two options, Settings and Log out, with similar semantics as
the desktop top bar.

Below the mobile top bar, a list of recent conversations appears. While in the
recent conversations screen on mobile, no active conversation is highlighted.
Tapping a recent conversation changes it to the active conversation and
switches to the mobile chat screen.

![Mobile recent conversations screen](http://i.imgur.com/YuXy3Ra.jpg)
*Image: The mobile recent conversations screen*

In the screen above, you can see a list of recent conversations, of which the
most recent conversation is the channel "chicken", and the second most recent
conversation is the channel "ting". The next two more recent conversations are
two private conversations with the users "gtklocker", who is online, and
"vitsalis", who is offline. The least recent conversation is the channel
"party".

In the mobile chat screen, a list of messages appears, which is rendered
similar to the desktop version. At the top of the list, the name of the
conversation appears in a separate title bar, along with a back button on the
left, which allows the user to return to the recent conversation list screen.

![Mobile chat screen](http://i.imgur.com/jECW8Jn.jpg)
*Image: The mobile chat screen*

# Typing
Ting provides a different approach from usual chat platforms when it comes to
notifications about typing. Users can see each other typing in real time. This
works as follows.

Messages in ting are separated into persistent and non-persistent. Persistent
messages are messages that have been sent. Non-persistent messages are messages
that are currently being typed, but have not been sent yet (the Enter key has
not been pressed by the user.) Users can see both persistent and non-persistent
messages and both are communicated on the network in real time.

When a user starts typing a message in a channel, they reserve a position in
the channel's history. Figuring out this position is critical for a smooth user
experience and is determined by the following rules.

* This position is maintained among other people who are currently typing, as
well as persistent messages that have been sent. When nobody is typing and a
user starts typing, this position becomes the end of the existing persistent
messages.

* When several users are typing and a user starts typing, their position becomes
at the end among the existingly typing users and after all persistent messages.

* When a user stops typing and erases their typed message, their position is
lost and their message is not persisted.

* When a user makes a message persistent by hitting the enter key, that
message's position in the history remains as-is among other users who are
typing. That is, it is not posted at the end of persistent messages, but
potentially among messages that have not yet been made persistent yet.

The user interface for this algorithm is different depending on whether the
current user or a remote user is typing. The non-persisted message of the
current user is displayed as "..." in the history portion of the chat. The full
message is displayed in the textarea as it is being typed. The "..." servers to
indicate to the user their current position among other typing users. Remote
non-persistent messages are displayed by the text being added in real time as
the user types, in their designated location.

Non-persistent messages are differentiated from persistent messages by showing
them as "ghosts", in a more transparent color. Additionally, the text of a
non-persistent message is slowly flashing by becoming more and less trasparent
to indicate that the message is ephemeral and currently changing.

![Desktop chat typing](http://i.imgur.com/9MdtAgp.jpg)
*Image: Desktop chat screen while typing*

![Mobile chat typing](http://i.imgur.com/IjDrJlY.jpg)
*Image: Mobile chat screen while typing*

# Settings screen
The settings screen allows a user to specify details about their user profile.

It consists of a form at the top and a save button with the title "Αποθήκευση"
at the bottom.

The form has the user's avatar displayed on the left. Below it is a button with
the title "Αλλαγή της εικόνας μου". Clicking it pops up a window allowing the
user to select a new avatar. The avatar is uploaded and displayed in the avatar
location within the settings. Before displaying it, the avatar is first cropped
into a square and then resized to fit the avatar size.

It is also possible for the user to upload an avatar by dragging a file onto
their avatar within their settings. While dragging a file over the screen, the
avatar location is changed into the text "Άφησε την εικόνα εδώ".

If the uploaded file is not a valid avatar, then the error message "Δοκίμασε
κάποια άλλη εικόνα" is displayed.

Next to the avatar, the username is displayed.

Below the avatar and the username, there are four labels associated with their
respective inputs. The inputs are prefilled with the settings the user has
entered previously.

The first label is "E-mail". The input is a text box. If the user has left this
field empty, a warning text appears above the label and the field stating:
"Γράψε το e-mail σου ώστε να μην χάσεις την πρόσβαση στο λογαριασμό σου".

The second label for the date of birth is "Ημερομηνία γέννησης". The input
consists of three select fields, for the day, the month, and the year. All
fields contain the range of valid numbers for days, months, and years
respectively, as well as the "-" option. The days allow selecting from 1 to 31
ascending, the months from 1 to 12 ascending, and the years from 1920 to the
current year descending.

The third label for the gender is "Φύλο". The input consists of a select field
with three options "Αγόρι", "Κορίτσι" and "-".

The fourth label for the location is "Περιοχή". The input is a select box
listing all the major cities of Greece as well as the option "-".

Clicking the save button validates the form as follows:

1. The e-mail address is validated for form with a simple validation algorithm
and not exhaustively. It must contain an `@` symbol. It must contain at least
one alphanumeric character before the `@` sumbol. It must contain at least
three characters after the `@` symbol, one of which must be a `.`. The e-mail
must be at most 128 characters. The user can also leave the e-mail address
empty if they do not wish to associate an e-mail address with their account.

2. The date of birth must be a valid date.

If the form fails to validate, the following error messages are displayed above
their respective fields and the fields are highlighted in red:

1. "Γράψε ένα έγκυρο e-mail" if the e-mail address is invalid.
2. "Δώσε μία έγκυρη ημερομηνία γέννησης" if the date of birth is invalid.

Otherwise, the form is saved and the user is taken back to the Chat screen.

Notice that multiple users can share the same e-mail address.

# Security
For transport security purposes, ting.gr is served over HTTPS.

# TODO
This specification is limited. It will be extended with the following features in future editions:

* Avatars
* Age / sex / location
* Voice
* Channel moderation
* Subscription to channels
* Image uploads
* Timestamps
* Smileys
