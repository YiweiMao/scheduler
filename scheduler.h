/*
 * File:   scheduler.h
 * Author: Tristan H
 */

#ifndef OS_H
#define	OS_H

typedef unsigned long ostime_t;

void initOS();

void run_later(void (*)(), ostime_t);

void run();

void blinkLED();

#endif	/* OS_H */
