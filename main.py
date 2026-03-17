from agent import StudyCoachAgent
from util.pretty_print import print_welcome, get_user_input


def main() -> None:
    agent = StudyCoachAgent()

    print_welcome(
        title="Study Coach Agent",
        description=(
            "A simple terminal agent that helps a student study a topic, "
            "understand concepts, and prepare for homework or exams."
        ),
        version="0.1.0",
    )

    print("Commands: exit, reset\n")

    while True:
        user_input = get_user_input("Ask your study question")

        if not user_input:
            continue

        if user_input.lower() == "exit":
            print("Goodbye.")
            break

        if user_input.lower() == "reset":
            agent.reset_memory()
            print("Conversation memory cleared.\n")
            continue

        try:
            answer = agent.chat(user_input)
            print(answer)
            print()
        except Exception as exc:
            print(f"Error: {exc}\n")


if __name__ == "__main__":
    main()
    