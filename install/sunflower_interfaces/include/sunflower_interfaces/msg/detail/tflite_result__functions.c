// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from sunflower_interfaces:msg/TfliteResult.idl
// generated code does not contain a copyright notice
#include "sunflower_interfaces/msg/detail/tflite_result__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


bool
sunflower_interfaces__msg__TfliteResult__init(sunflower_interfaces__msg__TfliteResult * msg)
{
  if (!msg) {
    return false;
  }
  // nose
  // eye_l
  // eye_r
  // ear_l
  // ear_r
  // shoulder_l
  // shoulder_r
  return true;
}

void
sunflower_interfaces__msg__TfliteResult__fini(sunflower_interfaces__msg__TfliteResult * msg)
{
  if (!msg) {
    return;
  }
  // nose
  // eye_l
  // eye_r
  // ear_l
  // ear_r
  // shoulder_l
  // shoulder_r
}

sunflower_interfaces__msg__TfliteResult *
sunflower_interfaces__msg__TfliteResult__create()
{
  sunflower_interfaces__msg__TfliteResult * msg = (sunflower_interfaces__msg__TfliteResult *)malloc(sizeof(sunflower_interfaces__msg__TfliteResult));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(sunflower_interfaces__msg__TfliteResult));
  bool success = sunflower_interfaces__msg__TfliteResult__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
sunflower_interfaces__msg__TfliteResult__destroy(sunflower_interfaces__msg__TfliteResult * msg)
{
  if (msg) {
    sunflower_interfaces__msg__TfliteResult__fini(msg);
  }
  free(msg);
}


bool
sunflower_interfaces__msg__TfliteResult__Sequence__init(sunflower_interfaces__msg__TfliteResult__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  sunflower_interfaces__msg__TfliteResult * data = NULL;
  if (size) {
    data = (sunflower_interfaces__msg__TfliteResult *)calloc(size, sizeof(sunflower_interfaces__msg__TfliteResult));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = sunflower_interfaces__msg__TfliteResult__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        sunflower_interfaces__msg__TfliteResult__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
sunflower_interfaces__msg__TfliteResult__Sequence__fini(sunflower_interfaces__msg__TfliteResult__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      sunflower_interfaces__msg__TfliteResult__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

sunflower_interfaces__msg__TfliteResult__Sequence *
sunflower_interfaces__msg__TfliteResult__Sequence__create(size_t size)
{
  sunflower_interfaces__msg__TfliteResult__Sequence * array = (sunflower_interfaces__msg__TfliteResult__Sequence *)malloc(sizeof(sunflower_interfaces__msg__TfliteResult__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = sunflower_interfaces__msg__TfliteResult__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
sunflower_interfaces__msg__TfliteResult__Sequence__destroy(sunflower_interfaces__msg__TfliteResult__Sequence * array)
{
  if (array) {
    sunflower_interfaces__msg__TfliteResult__Sequence__fini(array);
  }
  free(array);
}
