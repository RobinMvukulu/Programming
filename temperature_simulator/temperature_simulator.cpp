#include <iostream>
#include <cstdlib> // To generate rand
#include <ctime>   // To chose a seed for rand
#include <chrono>  // To do action every second
#include <thread>  // To force a pause of 1 second
#include <iomanip> // Set precision for .0
#include <sstream> // For date formating
#include <fstream> // For writing in file
#include <vector> // For arrays
#include <numeric> // For average value of a trend
#include <winsock2.h> // To create socket
#include <ws2tcpip.h>
#pragma comment(lib, "ws2_32.lib")


int main() {

	// INITIALISATION WINSOCK
    WSADATA wsaData;
    int result = WSAStartup(MAKEWORD(2, 2), &wsaData);
    if (result != 0) {
        std::cerr << "WSAStartup failed: " << result << std::endl;
        return 1;
    }
    
    // CREATE SOCKET
    SOCKET server_socket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    if (server_socket == INVALID_SOCKET) {
        std::cerr << "Socket creation failed." << std::endl;
        WSACleanup();
        return 1;
    }
    // SETUP SERVER PARAMETERS
    sockaddr_in server_addr = {};
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = inet_addr("127.0.0.1"); // localhost
    server_addr.sin_port = htons(12345); // Port local
    
    // CONNECTION
    if (bind(server_socket, (SOCKADDR*)&server_addr, sizeof(server_addr)) == SOCKET_ERROR) {
        std::cerr << "Bind failed." << std::endl;
        closesocket(server_socket);
        WSACleanup();
        return 1;
    }
    
    // LISTEN CLIENT
    listen(server_socket, SOMAXCONN);
    std::cout << "En attente d'une connexion..." << std::endl;
    
    // ACCEPT CONNECTION
    SOCKET client_socket = accept(server_socket, nullptr, nullptr);
    if (client_socket == INVALID_SOCKET) {
        std::cerr << "Accept failed." << std::endl;
        closesocket(server_socket);
        WSACleanup();
        return 1;
    }

    std::cout << "Client connecté !" << std::endl;
    
    
    
    
    
    std::vector< float > trend;
    float min = 20.0f;
    float max = 30.0f;
    int is_high = 0;

    std::srand(std::time(nullptr));
    std::ofstream file("temp_data.txt", std::ios::app);
    
    while (true) {
        time_t now = time(0);
        char* date_time = ctime(&now);
        float temperature = min + static_cast<float>(std::rand()) / RAND_MAX * (max - min);
        if (temperature > 28)
        	is_high = 1;
        else
        	is_high = 0;
        if (trend.size() <= 10)
        	trend.push_back(temperature);
        else{
        	trend.erase(trend.begin());
        	trend.push_back(temperature);
        }
        float sum = std::accumulate(trend.begin(), trend.end(), 0.1f);
        float av = sum / trend.size();
        
        
        std::tm t = {};
    	std::istringstream ss(date_time);
    	ss >> std::get_time(&t, "%a %b %d %H:%M:%S %Y");
    	std::ostringstream formatted_date;
    	formatted_date << std::put_time(&t, "%Y-%m-%d %H-%M-%S");
    	
    	std::ostringstream ss_temp;
		ss_temp << std::fixed << std::setprecision(1) << temperature;
		std::string temp_str = ss_temp.str();

    	std::ostringstream ss_av;
		ss_av << std::fixed << std::setprecision(1) << av;
		std::string av_str = ss_av.str();

	    std::string line = formatted_date.str() + "," + temp_str + "," + av_str + "," + std::to_string(is_high) + ";\n";
	    file << line;
	    send(client_socket, line.c_str(), line.size(), 0);
	    std::cout << "Sent: " << line;
	    std::this_thread::sleep_for(std::chrono::seconds(1));
	}
	// CLEANUP
    closesocket(client_socket);
    std::cout << "Client déconnecté !" << std::endl;
    closesocket(server_socket);
    WSACleanup();
    file.close();
    return 0;
}
