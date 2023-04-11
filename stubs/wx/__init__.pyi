from __future__ import annotations

from typing import overload

ObjectRefData = object
""" Reference data, not enough data to get precise type info """


class ClassInfo:
	"""
	This class stores meta-information about classes.

	Instances of this class are not generally defined directly by an application, but indirectly through use of macros such as DECLARE_DYNAMIC_CLASS and IMPLEMENT_DYNAMIC_CLASS.
	"""

	def CreateObject( self ) -> Object:
		"""
		Creates an object of the appropriate kind.
		\t
		:return: None if the class has not been declared dynamically creatable (typically, this happens for abstract classes).
		"""

	@staticmethod
	def FindClass( className: str ) -> ClassInfo:
		"""
		Finds the wx.ClassInfo object for a class with the given name.
		\t
		:param className:
		:return:
		"""

	def GetBaseClassName1( self ) -> str:
		"""
		Returns the name of the first base class (None if none).
		\t
		:return:
		"""

	def GetBaseClassName2( self ) -> str:
		"""
		Returns the name of the second base class (None if none).
		\t
		:return:
		"""

	def GetClassName( self ) -> str:
		"""
		Returns the string form of the class name.
		\t
		:return:
		"""

	def GetSize( self ) -> int:
		"""
		Returns the size of the class.
		"""

	def IsDynamic( self ) -> bool:
		"""
		Returns True if this class info can create objects of the associated class.
		\t
		:return:
		"""

	def IsKindOf( self, info: ClassInfo ) -> bool:
		"""
		Returns True if this class is a kind of (inherits from) the given class.
		\t
		:param info:
		:return:
		"""


class Object:
	""" This is the root class of many of the wxWidgets classes. """

	@overload
	def __init__( self ) -> None:
		"""
		Default constructor; initializes to None the internal reference data.
		"""

	def __init__( self, other: Object ) -> None:
		"""
		Sets the internal Object.m_refData pointer to point to the same instance of the ObjectRefData-derived class pointed by other and increments the refcount of Object.m_refData.
		\t
		:param other:
		"""

	def Destroy( self ) -> None:
		"""
		Deletes the C++ object this Python object is a proxy for.
		"""

	def GetClassInfo( self ) -> ClassInfo:
		"""
		This virtual function is redefined for every class that requires run-time type information, when using the DECLARE_CLASS macro (or similar).
		"""

	def GetClassName( self ) -> str:
		"""
		Returns the class name of the C++ class using RTTI
		\t
		:return:
		"""

	def GetRefData( self ) -> ObjectRefData:
		"""
		Returns the Object.m_refData pointer, i.e. the data referenced by this object.
		\t
		:return:
		"""

	def IsSameAs( self, obj: Object ) -> bool:
		"""
		Returns True if this object has the same data pointer as obj.

		Notice that True is returned if the data pointers are None in both objects.

		This function only does a shallow comparison, i.e. it doesn’t compare the objects pointed to by the data pointers of these objects.
		\t
		:param obj:
		:return:
		"""

	def Ref( self, clone: Object ) -> None:
		"""
		Makes this object refer to the data in clone.
		\t
		:param clone: The object to ‘clone’.
		"""

	def SetRefData( self, data: ObjectRefData ) -> None:
		"""
		Sets the Object.m_refData pointer.
		\t
		:param data:
		:return:
		"""

	def UnRef( self ) -> None:
		"""
		Decrements the reference count in the associated data, and if it is zero, deletes the data.

		The Object.m_refData member is set to None.
		\t
		:return:
		"""

	def UnShare( self ) -> None:
		"""
		This is the same of AllocExclusive but this method is public.
		\t
		:return:
		"""


class Trackable:
	"""
	Add-on base class for a trackable object.

	This class maintains an internal linked list of classes of type TrackerNode and calls OnObjectDestroy() on them if this object is destroyed. The most common usage is by using the WeakRef class template which automates this. This class has no public API. Its only use is by deriving another class from it to make it trackable.
	"""


class UniChar:
	"""
	This class represents a single Unicode character.

	It can be converted to and from char or wchar_t and implements commonly used character operations.
	"""

	def GetAsChar( self, c: int ) -> bool:
		"""
		Returns True if the character is representable as a single byte in the current locale encoding.

		This function only returns True if the character can be converted in exactly one byte, e.g. it only returns True for 7 bit ASCII characters when the encoding used is UTF-8.

		It is mostly useful to test if the character can be passed to functions taking a int and is used by wxWidgets itself for this purpose.
		\t
		:param c: An output pointer to the value of this Unicode character as a char . Must be not None.
		:return: True if the object is an 8 bit int and c was filled with its value as int or False otherwise (c won’t be modified then).
		"""

	def GetValue( self ) -> int:
		"""
		Returns Unicode code point value of the character.
		\t
		:return:
		"""

	@overload
	def HighSurrogate( self ) -> int:
		"""
		Returns the high surrogate code unit for the supplementary character.
		\t
		:return:
		"""

	def HighSurrogate( self, value ) -> int:
		"""
		Returns the high surrogate code unit for the supplementary character.
		\t
		:param value: The Unicode code point of the character.
		:return:
		"""

	def IsAscii( self ) -> bool:
		"""
		Returns True if the character is an ASCII character (i.e. if its value is less than 128).
		\t
		:return:
		"""



def GetApp() -> App: ...


class PyApp:
	pass


class App( PyApp ):
	...
