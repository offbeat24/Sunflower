// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from sunflower_interfaces:msg/TfliteResult.idl
// generated code does not contain a copyright notice

#ifndef SUNFLOWER_INTERFACES__MSG__DETAIL__TFLITE_RESULT__STRUCT_H_
#define SUNFLOWER_INTERFACES__MSG__DETAIL__TFLITE_RESULT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'nose'
// Member 'eye_l'
// Member 'eye_r'
// Member 'ear_l'
// Member 'ear_r'
// Member 'shoulder_l'
// Member 'shoulder_r'
#include "rosidl_runtime_c/primitives_sequence.h"

// Struct defined in msg/TfliteResult in the package sunflower_interfaces.
typedef struct sunflower_interfaces__msg__TfliteResult
{
  rosidl_runtime_c__float__Sequence nose;
  rosidl_runtime_c__float__Sequence eye_l;
  rosidl_runtime_c__float__Sequence eye_r;
  rosidl_runtime_c__float__Sequence ear_l;
  rosidl_runtime_c__float__Sequence ear_r;
  rosidl_runtime_c__float__Sequence shoulder_l;
  rosidl_runtime_c__float__Sequence shoulder_r;
} sunflower_interfaces__msg__TfliteResult;

// Struct for a sequence of sunflower_interfaces__msg__TfliteResult.
typedef struct sunflower_interfaces__msg__TfliteResult__Sequence
{
  sunflower_interfaces__msg__TfliteResult * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sunflower_interfaces__msg__TfliteResult__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SUNFLOWER_INTERFACES__MSG__DETAIL__TFLITE_RESULT__STRUCT_H_
