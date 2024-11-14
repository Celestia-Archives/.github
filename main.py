# main.py
from actions import wisdom, cosmic_events, reflection, time_mysteries

def main():
    print("Celestia: Welcome, Earthling. Ask me of the cosmos, and I shall respond.")
    while True:
        user_input = input("You: ").lower()
        
        if "wisdom" in user_input:
            print(f"Celestia: {wisdom.share_wisdom()}")
        elif "event" in user_input or "cosmic" in user_input:
            print(f"Celestia: {cosmic_events.describe_cosmic_event()}")
        elif "reflect" in user_input or "question" in user_input:
            print(f"Celestia: {reflection.offer_reflection()}")
        elif "time" in user_input or "mystery" in user_input:
            print(f"Celestia: {time_mysteries.ponder_time()}")
        elif user_input in ["exit", "quit"]:
            print("Celestia: Farewell, Earthling. May the stars guide you.")
            break
        else:
            print("Celestia: I sense a question, but it is beyond my archives. Try asking differently.")

if __name__ == "__main__":
    main()
