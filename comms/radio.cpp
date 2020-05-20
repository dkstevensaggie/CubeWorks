#include "radio.hpp"

std::vector<int> Radio::receive() {
	// return start and end range for db query 
	return std::vector<int> {};
}

void Radio::transmit() {
	// invoke radio with data cache file
}

std::string Radio::packetize() {
	// packetize retreived data
	return "";
}

void Radio::retreive(int start, int end) {
	// get data from start to end from this.dbPath calls this.packetize(retrieved data)
}
