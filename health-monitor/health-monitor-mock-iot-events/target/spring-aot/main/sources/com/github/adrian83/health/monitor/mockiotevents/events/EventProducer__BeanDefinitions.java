package com.github.adrian83.health.monitor.mockiotevents.events;

import org.springframework.aot.generate.Generated;
import org.springframework.beans.factory.config.BeanDefinition;
import org.springframework.beans.factory.support.RootBeanDefinition;

/**
 * Bean definitions for {@link EventProducer}.
 */
@Generated
public class EventProducer__BeanDefinitions {
  /**
   * Get the bean definition for 'eventProducer'.
   */
  public static BeanDefinition getEventProducerBeanDefinition() {
    RootBeanDefinition beanDefinition = new RootBeanDefinition(EventProducer.class);
    beanDefinition.setInstanceSupplier(EventProducer::new);
    return beanDefinition;
  }
}
