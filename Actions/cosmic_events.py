# cosmic_events.py
import random

def describe_cosmic_event():
    events = [
        "A supernova explodes, scattering stardust across the universe, seeding life anew.",
        "A black hole pulls in all light and matter nearby, a reminder of the universe's boundless mystery.",
        "A new star is born in a nebula, its light beginning a journey across the cosmos."
    ]
    return random.choice(events)
