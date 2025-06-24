package com.github.adrian83.health.monitor.mockiotevents;

import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class Runner implements CommandLineRunner {

    @Override
    public void run(String... args) {
        System.out.println("Running AWS Batch job logic...");
        // logic
    }
}