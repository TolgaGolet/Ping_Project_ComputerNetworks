# Ping_Project_ComputerNetworks

This project aims to measure ping times by sending packets to certain destinations from a certain source and observe how the round trip time values are changed while the testing days and hours varies. To make this experiment, 10 distinct destinations and 1 source location were predetermined through the experiment. And also 100 packets were sent for each pinging test/destination and average values were calculated. It means that 1000 packets in total were sent per hour in this test. (100 for each destination.). 7 days spent for this project and made ping tests 4 hours a day which means tested 28 hours and sent 28,000 packets in total. For this purpose, the ping experiment was automatized using Python. Once the software starts, it waits for the testing times and automatically starts to ping (100 packets) for each predetermined destination by order and automatically logs the results to a text file. Average values were automatically calculated by the ping command in Windows. I usually made sure that there is no another connected device on the same local network which communicates with the internet.

# Screenshots

![screenshot](https://github.com/TolgaGolet/Ping_Project_ComputerNetworks/blob/master/Screenshots/Screenshot.png)

# Conclusion

When we observe the results carefully, we usually get approximately the same response times from the same IP addresses. But we may see little changes throughout the days and hours. I think that those little changes occur because of the number of people trying to make request to the same IP address or same routes. Distance is not the most effective parameter which is explained under the first results table. We also conclude that if there is another device on the same local network which makes any data communication with the internet, causes very big affect and increases response time considerably. Especially streaming videos or downloading files makes the biggest affect. This situation even causes packet losses.
