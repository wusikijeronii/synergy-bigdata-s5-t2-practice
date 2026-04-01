#include <iostream>
#include <string>
#include <vector>

struct PowerSupplyData
{
    double temperature_c = 0.0;
    double load_percent = 0.0;
    double power_watts = 0.0;
    double voltage = 0.0;
    int fan_rpm = 0;
};

struct DiagnosticResult
{
    std::vector<std::string> warnings;
    std::string status;
};

DiagnosticResult diagnose(const PowerSupplyData &data)
{
    DiagnosticResult result;

    if (data.temperature_c >= 80.0) result.warnings.push_back("High temperature detected.");
    else if (data.temperature_c >= 65.0) result.warnings.push_back("Temperature is above normal.");

    if (data.load_percent >= 95.0) result.warnings.push_back("Critical load level.");
    else if (data.load_percent >= 80.0) result.warnings.push_back("High load level.");

    if (data.power_watts >= 750.0) result.warnings.push_back("Power consumption is very high.");
    else if (data.power_watts >= 600.0) result.warnings.push_back("Power consumption is above normal.");

    if (data.voltage < 11.4) result.warnings.push_back("Voltage is too low.");
    else if (data.voltage > 12.6) result.warnings.push_back("Voltage is too high.");

    if (data.fan_rpm < 700) result.warnings.push_back("Fan speed is too low.");

    if (result.warnings.empty()) result.status = "Power supply status: OK";
    else if (result.warnings.size() <= 2) result.status = "Power supply status: Warning";
    else result.status = "Power supply status: Critical";

    return result;
}

int main()
{
    PowerSupplyData data;

    std::cout << "Power Supply Diagnostics\n";
    std::cout << "Enter temperature (C): ";
    std::cin >> data.temperature_c;

    std::cout << "Enter load (%): ";
    std::cin >> data.load_percent;

    std::cout << "Enter power consumption (W): ";
    std::cin >> data.power_watts;

    std::cout << "Enter voltage (V): ";
    std::cin >> data.voltage;

    std::cout << "Enter fan speed (RPM): ";
    std::cin >> data.fan_rpm;

    DiagnosticResult result = diagnose(data);

    std::cout << "\n" << result.status << "\n";

    if (!result.warnings.empty())
    {
        std::cout << "Detected issues:\n";
        for (const auto &warning : result.warnings) std::cout << "- " << warning << "\n";
    }
    else std::cout << "No issues detected.\n";

    return 0;
}