from PySide6.QtCore import QObject

class Annotation(QObject):
	def __init__(self, annotation: dict=None):
		super().__init__()

		self.__annotation = annotation if annotation is not None else {
			"statement": "",
			"verdict": 1,
			"evidence": "",
			"start": 0,
			"end": 0
		}

	@property
	def annotation(self):
		return self.__annotation

	@property
	def statement(self) -> str:
		return self.__annotation["statement"]

	def setStatement(self, value: str) -> None:
		self.__annotation["statement"] = value

	@property
	def verdict(self) -> int:
		return self.__annotation["verdict"] if self.__annotation is not None else 0

	def setVerdict(self, value: int) -> None:
		self.__annotation["verdict"] = value

	@property
	def evidence(self) -> str:
		return self.__annotation["evidence"] if self.__annotation is not None else ""

	def setEvidence(self, value: str) -> None:
		self.__annotation["evidence"] = value

	@property
	def startIndex(self) -> int:
		return self.__annotation["start"]

	def setStartIndex(self, value: int) -> None:
		self.__annotation["start"] = value

	@property
	def endIndex(self) -> int:
		return self.__annotation["end"]

	def setEndIndex(self, value: int) -> None:
		self.__annotation["end"] = value

	def __str__(self) -> str:
		return self.__annotation.__str__()
