package com.github.adrian83.health.monitor.mockiotevents;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MockIoTEventsApp { //implements CommandLineRunner {

    public static void main(String[] args) {
        SpringApplication.run(MockIoTEventsApp.class, args);
    }

    // @Override
    // public void run(String... args) {
    //     System.out.println("Running AWS Batch job logic...");
    //     // logic
    // }
}