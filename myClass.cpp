// ConsoleApplication22.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

namespace myNamespcae {
	class myClass {
	public:
		void print()
		{
			printf("Halló Daniel");
		}
	};
}

int main()
{
	myNamespcae::myClass *c = new myNamespcae::myClass();
	c->print();
	while (true)
	{

	}
    return 0;
}

