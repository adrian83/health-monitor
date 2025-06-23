package com.github.adrian83.health.monitor.mockiotevents.job;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
public class EventSender {

    private static final Logger LOGGER = LogManager.getLogger(EventSender.class);


    //@Scheduled(fixedRate = 5000)
    public void sendEvent() {
        LOGGER.info("Sending event to IoT");
    }

}