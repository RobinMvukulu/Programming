#include <iostream>
#include <chrono>  // To do action every second
#include <thread>  // To force a pause of 1 second
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
    std::cout << "Client connected !" << std::endl;

    char buffer[1024];
    int bytesReceived;

    while (true) {
        ZeroMemory(buffer, sizeof(buffer));

        bytesReceived = recv(client_socket, buffer, sizeof(buffer), 0);
        std::cout << bytesReceived << std::endl;



    // Cleanup
    closesocket(client_socket);
    closesocket(server_socket);
    WSACleanup();

    return 0;
    }
}
