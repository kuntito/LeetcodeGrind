i'm given a list of meetings.

each meeting is represented by 
    it's start time, and
    it's end time.

each meeting is assigned a room.
that's where the meeting happens.

my job is to find the room that held the most meetings.

for this, i need to understand how the meetings are assigned to rooms.

the meetings are assigned to the next available room.
and what does next available mean?

the first room that can hold a meeting.

what does first room mean?
well, the rooms are numbered from `0` till `n-1`

and the first room is decided left to right.
the first available room is `room 0`.

i want to place the next meeting in the first available room.

what is the next meeting?
the next meeting is the earliest meeting.

i don't think you would have to clarify what next room means
if the meetings were visibly itemized.

you'd, by default list them in sorted order.

so, you always want to put the next meeting in the next available room.
what does available mean?

the first vacant room.

`TODO define available room`