package com.github.adrian83.health.monitor.mockiotevents;

import org.springframework.aot.generate.Generated;
import org.springframework.beans.factory.config.BeanDefinition;
import org.springframework.beans.factory.support.RootBeanDefinition;

/**
 * Bean definitions for {@link MockIoTEventsApp}.
 */
@Generated
public class MockIoTEventsApp__BeanDefinitions {
  /**
   * Get the bean definition for 'mockIoTEventsApp'.
   */
  public static BeanDefinition getMockIoTEventsAppBeanDefinition() {
    RootBeanDefinition beanDefinition = new RootBeanDefinition(MockIoTEventsApp.class);
    beanDefinition.setInstanceSupplier(MockIoTEventsApp::new);
    return beanDefinition;
  }
}
