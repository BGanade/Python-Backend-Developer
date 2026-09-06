""" Futuro Eventos, a company specialized in conference organization, made a mistake
when recording the sequence of events for an important conference. The events were
recorded in the reverse order of how they were supposed to happen. Now, the team
needs to correct the order of the events to ensure that the conference follows
the original plan.

Considering the initial list of events, create a program that allows the organizer
to reorder them so that the final list follows the correct sequence.

Example:

registered_events = ['Closing Ceremony', 'Lecture 3', 'Lecture 2', 'Opening Ceremony']

Expected Output:

Corrected order: ['Opening Ceremony', 'Lecture 2', 'Lecture 3', 'Closing Ceremony'] """

registered_events = ['Closing Ceremony',
                     'Lecture 3', 'Lecture 2', 'Opening Ceremony']
registered_events.reverse()
print(registered_events)
