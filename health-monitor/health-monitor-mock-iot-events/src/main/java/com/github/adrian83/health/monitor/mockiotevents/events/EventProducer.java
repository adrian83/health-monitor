package com.github.adrian83.health.monitor.mockiotevents.events;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.springframework.stereotype.Component;

@Component
public class EventProducer {

    private static final Logger LOGGER = LogManager.getLogger(EventProducer.class);


    public void sendEvent() {
        LOGGER.info("Sending event to IoT");
    }

}