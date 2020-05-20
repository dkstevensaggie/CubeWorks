#ifndef RADIO_HPP
#define RADIO_HPP

#include <vector>
#include <string>

class Radio {
	public:
		Radio(std::string dbPath) :
			dbPath(dbPath)
		{};
		std::vector<int> receive();
		void transmit();
		void packetize();
		void retreive(int start, int end);
	
	private:
		std::string dbPath;
};

#endif
