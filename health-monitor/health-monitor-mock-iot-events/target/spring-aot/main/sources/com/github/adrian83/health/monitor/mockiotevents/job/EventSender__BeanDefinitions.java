package com.github.adrian83.health.monitor.mockiotevents.job;

import org.springframework.aot.generate.Generated;
import org.springframework.beans.factory.config.BeanDefinition;
import org.springframework.beans.factory.support.RootBeanDefinition;

/**
 * Bean definitions for {@link EventSender}.
 */
@Generated
public class EventSender__BeanDefinitions {
  /**
   * Get the bean definition for 'eventSender'.
   */
  public static BeanDefinition getEventSenderBeanDefinition() {
    RootBeanDefinition beanDefinition = new RootBeanDefinition(EventSender.class);
    beanDefinition.setInstanceSupplier(EventSender::new);
    return beanDefinition;
  }
}
