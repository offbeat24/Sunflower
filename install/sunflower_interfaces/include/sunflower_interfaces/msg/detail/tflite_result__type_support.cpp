// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from sunflower_interfaces:msg/TfliteResult.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "sunflower_interfaces/msg/detail/tflite_result__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace sunflower_interfaces
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void TfliteResult_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) sunflower_interfaces::msg::TfliteResult(_init);
}

void TfliteResult_fini_function(void * message_memory)
{
  auto typed_message = static_cast<sunflower_interfaces::msg::TfliteResult *>(message_memory);
  typed_message->~TfliteResult();
}

size_t size_function__TfliteResult__nose(const void * untyped_member)
{
  (void)untyped_member;
  return 3;
}

const void * get_const_function__TfliteResult__nose(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<float, 3> *>(untyped_member);
  return &member[index];
}

void * get_function__TfliteResult__nose(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<float, 3> *>(untyped_member);
  return &member[index];
}

size_t size_function__TfliteResult__eye_l(const void * untyped_member)
{
  (void)untyped_member;
  return 3;
}

const void * get_const_function__TfliteResult__eye_l(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<float, 3> *>(untyped_member);
  return &member[index];
}

void * get_function__TfliteResult__eye_l(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<float, 3> *>(untyped_member);
  return &member[index];
}

size_t size_function__TfliteResult__eye_r(const void * untyped_member)
{
  (void)untyped_member;
  return 3;
}

const void * get_const_function__TfliteResult__eye_r(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<float, 3> *>(untyped_member);
  return &member[index];
}

void * get_function__TfliteResult__eye_r(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<float, 3> *>(untyped_member);
  return &member[index];
}

size_t size_function__TfliteResult__ear_l(const void * untyped_member)
{
  (void)untyped_member;
  return 3;
}

const void * get_const_function__TfliteResult__ear_l(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<float, 3> *>(untyped_member);
  return &member[index];
}

void * get_function__TfliteResult__ear_l(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<float, 3> *>(untyped_member);
  return &member[index];
}

size_t size_function__TfliteResult__ear_r(const void * untyped_member)
{
  (void)untyped_member;
  return 3;
}

const void * get_const_function__TfliteResult__ear_r(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<float, 3> *>(untyped_member);
  return &member[index];
}

void * get_function__TfliteResult__ear_r(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<float, 3> *>(untyped_member);
  return &member[index];
}

size_t size_function__TfliteResult__shoulder_l(const void * untyped_member)
{
  (void)untyped_member;
  return 3;
}

const void * get_const_function__TfliteResult__shoulder_l(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<float, 3> *>(untyped_member);
  return &member[index];
}

void * get_function__TfliteResult__shoulder_l(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<float, 3> *>(untyped_member);
  return &member[index];
}

size_t size_function__TfliteResult__shoulder_r(const void * untyped_member)
{
  (void)untyped_member;
  return 3;
}

const void * get_const_function__TfliteResult__shoulder_r(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<float, 3> *>(untyped_member);
  return &member[index];
}

void * get_function__TfliteResult__shoulder_r(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<float, 3> *>(untyped_member);
  return &member[index];
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember TfliteResult_message_member_array[7] = {
  {
    "nose",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    3,  // array size
    false,  // is upper bound
    offsetof(sunflower_interfaces::msg::TfliteResult, nose),  // bytes offset in struct
    nullptr,  // default value
    size_function__TfliteResult__nose,  // size() function pointer
    get_const_function__TfliteResult__nose,  // get_const(index) function pointer
    get_function__TfliteResult__nose,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "eye_l",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    3,  // array size
    false,  // is upper bound
    offsetof(sunflower_interfaces::msg::TfliteResult, eye_l),  // bytes offset in struct
    nullptr,  // default value
    size_function__TfliteResult__eye_l,  // size() function pointer
    get_const_function__TfliteResult__eye_l,  // get_const(index) function pointer
    get_function__TfliteResult__eye_l,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "eye_r",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    3,  // array size
    false,  // is upper bound
    offsetof(sunflower_interfaces::msg::TfliteResult, eye_r),  // bytes offset in struct
    nullptr,  // default value
    size_function__TfliteResult__eye_r,  // size() function pointer
    get_const_function__TfliteResult__eye_r,  // get_const(index) function pointer
    get_function__TfliteResult__eye_r,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "ear_l",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    3,  // array size
    false,  // is upper bound
    offsetof(sunflower_interfaces::msg::TfliteResult, ear_l),  // bytes offset in struct
    nullptr,  // default value
    size_function__TfliteResult__ear_l,  // size() function pointer
    get_const_function__TfliteResult__ear_l,  // get_const(index) function pointer
    get_function__TfliteResult__ear_l,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "ear_r",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    3,  // array size
    false,  // is upper bound
    offsetof(sunflower_interfaces::msg::TfliteResult, ear_r),  // bytes offset in struct
    nullptr,  // default value
    size_function__TfliteResult__ear_r,  // size() function pointer
    get_const_function__TfliteResult__ear_r,  // get_const(index) function pointer
    get_function__TfliteResult__ear_r,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "shoulder_l",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    3,  // array size
    false,  // is upper bound
    offsetof(sunflower_interfaces::msg::TfliteResult, shoulder_l),  // bytes offset in struct
    nullptr,  // default value
    size_function__TfliteResult__shoulder_l,  // size() function pointer
    get_const_function__TfliteResult__shoulder_l,  // get_const(index) function pointer
    get_function__TfliteResult__shoulder_l,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "shoulder_r",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    3,  // array size
    false,  // is upper bound
    offsetof(sunflower_interfaces::msg::TfliteResult, shoulder_r),  // bytes offset in struct
    nullptr,  // default value
    size_function__TfliteResult__shoulder_r,  // size() function pointer
    get_const_function__TfliteResult__shoulder_r,  // get_const(index) function pointer
    get_function__TfliteResult__shoulder_r,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers TfliteResult_message_members = {
  "sunflower_interfaces::msg",  // message namespace
  "TfliteResult",  // message name
  7,  // number of fields
  sizeof(sunflower_interfaces::msg::TfliteResult),
  TfliteResult_message_member_array,  // message members
  TfliteResult_init_function,  // function to initialize message memory (memory has to be allocated)
  TfliteResult_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t TfliteResult_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &TfliteResult_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace sunflower_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<sunflower_interfaces::msg::TfliteResult>()
{
  return &::sunflower_interfaces::msg::rosidl_typesupport_introspection_cpp::TfliteResult_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, sunflower_interfaces, msg, TfliteResult)() {
  return &::sunflower_interfaces::msg::rosidl_typesupport_introspection_cpp::TfliteResult_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
