C header file generator
#######################

This tool reads a C source file (.c) and generates the text for the corresponding
header file, with function declarations for any non-static function definitions
found in the provided C file.


Usage
=====

Execute cheaders through the python interpreter as a module:

::

    python -m cheaders source_file.c


Example output
==============

The following example shows what is generated for a sample ``.c`` file. The
sample file is called ``ulist_.c``, and contains the following code:


Example C source file
---------------------

.. code:: c

	int myfunction(int intvar, float floatvar)
	{
		// Do important stuff
		return 0;
	}


	void myotherfunction(int intvar, float floatvar, char long_name_variable)
	{
		// Do other important stuff
	}


The header file that will be generated, with doxygen comments enabled (the
default) looks like this:


Generated header file
---------------------

.. code:: c

	/*
	 * myfile.h
	 *
	 * (Description here)
	 *
	 */


	#ifndef MYFILE_H
	#define MYFILE_H


	/**
	 * (Description)
	 *
	 * @param   intvar      (description)
	 * @param   floatvar    (description)
	 *
	 * @return  (description)
	 */
	int myfunction(int intvar, float floatvar);


	/**
	 * (Description)
	 *
	 * @param   intvar              (description)
	 * @param   floatvar            (description)
	 * @param   long_name_variable  (description)
	 */
	void myotherfunction(int intvar, float floatvar, char long_name_variable);


	#endif /* MYFILE_H */

