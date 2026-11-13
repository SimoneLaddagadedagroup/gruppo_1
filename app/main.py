from app.task_service import aggiungi_task, completa_task
from app.task_report import riepilogo

# commento 1
# commento 2
# new featured added - Reza
# new comment from reza.
<<<<<<< HEAD
=======

#main modified
#main modified again
>>>>>>> 72a5e0e (fied main issue)
def main() -> None:
    tasks = []
    aggiungi_task(tasks, "Preparare backlog", "Anna")
    aggiungi_task(tasks, "Scrivere test", "Marco")
    completa_task(tasks, 1)
    print(riepilogo(tasks))
    for task in tasks:
        stato = "OK" if task.completato else "DA FARE"
        print(f"[{stato}] #{task.id}: {task.titolo} ({task.assegnatario})")


if __name__ == "__main__":
    main()


CIAO
