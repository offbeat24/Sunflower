// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from sunflower_interfaces:msg/TfliteResult.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "sunflower_interfaces/msg/detail/tflite_result__rosidl_typesupport_introspection_c.h"
#include "sunflower_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "sunflower_interfaces/msg/detail/tflite_result__functions.h"
#include "sunflower_interfaces/msg/detail/tflite_result__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void TfliteResult__rosidl_typesupport_introspection_c__TfliteResult_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  sunflower_interfaces__msg__TfliteResult__init(message_memory);
}

void TfliteResult__rosidl_typesupport_introspection_c__TfliteResult_fini_function(void * message_memory)
{
  sunflower_interfaces__msg__TfliteResult__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember TfliteResult__rosidl_typesupport_introspection_c__TfliteResult_message_member_array[7] = {
  {
    "nose",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    3,  // array size
    false,  // is upper bound
    offsetof(sunflower_interfaces__msg__TfliteResult, nose),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "eye_l",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    3,  // array size
    false,  // is upper bound
    offsetof(sunflower_interfaces__msg__TfliteResult, eye_l),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "eye_r",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    3,  // array size
    false,  // is upper bound
    offsetof(sunflower_interfaces__msg__TfliteResult, eye_r),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "ear_l",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    3,  // array size
    false,  // is upper bound
    offsetof(sunflower_interfaces__msg__TfliteResult, ear_l),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "ear_r",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    3,  // array size
    false,  // is upper bound
    offsetof(sunflower_interfaces__msg__TfliteResult, ear_r),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "shoulder_l",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    3,  // array size
    false,  // is upper bound
    offsetof(sunflower_interfaces__msg__TfliteResult, shoulder_l),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "shoulder_r",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    3,  // array size
    false,  // is upper bound
    offsetof(sunflower_interfaces__msg__TfliteResult, shoulder_r),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers TfliteResult__rosidl_typesupport_introspection_c__TfliteResult_message_members = {
  "sunflower_interfaces__msg",  // message namespace
  "TfliteResult",  // message name
  7,  // number of fields
  sizeof(sunflower_interfaces__msg__TfliteResult),
  TfliteResult__rosidl_typesupport_introspection_c__TfliteResult_message_member_array,  // message members
  TfliteResult__rosidl_typesupport_introspection_c__TfliteResult_init_function,  // function to initialize message memory (memory has to be allocated)
  TfliteResult__rosidl_typesupport_introspection_c__TfliteResult_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t TfliteResult__rosidl_typesupport_introspection_c__TfliteResult_message_type_support_handle = {
  0,
  &TfliteResult__rosidl_typesupport_introspection_c__TfliteResult_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_sunflower_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sunflower_interfaces, msg, TfliteResult)() {
  if (!TfliteResult__rosidl_typesupport_introspection_c__TfliteResult_message_type_support_handle.typesupport_identifier) {
    TfliteResult__rosidl_typesupport_introspection_c__TfliteResult_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &TfliteResult__rosidl_typesupport_introspection_c__TfliteResult_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
