from dataclasses import dataclass


@dataclass
class Task:
    id: int
    titolo: str
    completato: bool = False
    assegnatario: str = ""

class Task2:
    id: int
    titolo: str
    completato: bool = True
    assegnatario: str = ""

class Task3:
    id: int
    titolo: str
    completato: bool = True
    assegnatario: str = ""

class Task4:
    id: int
    titolo: str
    completato: bool = True
    assegnatario: str = ""

class Task5:
    id: int
    titolo: str
    completato: bool = True
    assegnatario: str = ""