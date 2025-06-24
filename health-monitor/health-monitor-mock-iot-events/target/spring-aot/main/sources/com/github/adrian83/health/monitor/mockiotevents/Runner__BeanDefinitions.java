package com.github.adrian83.health.monitor.mockiotevents;

import org.springframework.aot.generate.Generated;
import org.springframework.beans.factory.config.BeanDefinition;
import org.springframework.beans.factory.support.RootBeanDefinition;

/**
 * Bean definitions for {@link Runner}.
 */
@Generated
public class Runner__BeanDefinitions {
  /**
   * Get the bean definition for 'runner'.
   */
  public static BeanDefinition getRunnerBeanDefinition() {
    RootBeanDefinition beanDefinition = new RootBeanDefinition(Runner.class);
    beanDefinition.setInstanceSupplier(Runner::new);
    return beanDefinition;
  }
}
