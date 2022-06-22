// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from sunflower_interfaces:msg/TfliteResult.idl
// generated code does not contain a copyright notice

#ifndef SUNFLOWER_INTERFACES__MSG__DETAIL__TFLITE_RESULT__STRUCT_HPP_
#define SUNFLOWER_INTERFACES__MSG__DETAIL__TFLITE_RESULT__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__sunflower_interfaces__msg__TfliteResult __attribute__((deprecated))
#else
# define DEPRECATED__sunflower_interfaces__msg__TfliteResult __declspec(deprecated)
#endif

namespace sunflower_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TfliteResult_
{
  using Type = TfliteResult_<ContainerAllocator>;

  explicit TfliteResult_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit TfliteResult_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _nose_type =
    std::vector<float, typename ContainerAllocator::template rebind<float>::other>;
  _nose_type nose;
  using _eye_l_type =
    std::vector<float, typename ContainerAllocator::template rebind<float>::other>;
  _eye_l_type eye_l;
  using _eye_r_type =
    std::vector<float, typename ContainerAllocator::template rebind<float>::other>;
  _eye_r_type eye_r;
  using _ear_l_type =
    std::vector<float, typename ContainerAllocator::template rebind<float>::other>;
  _ear_l_type ear_l;
  using _ear_r_type =
    std::vector<float, typename ContainerAllocator::template rebind<float>::other>;
  _ear_r_type ear_r;
  using _shoulder_l_type =
    std::vector<float, typename ContainerAllocator::template rebind<float>::other>;
  _shoulder_l_type shoulder_l;
  using _shoulder_r_type =
    std::vector<float, typename ContainerAllocator::template rebind<float>::other>;
  _shoulder_r_type shoulder_r;

  // setters for named parameter idiom
  Type & set__nose(
    const std::vector<float, typename ContainerAllocator::template rebind<float>::other> & _arg)
  {
    this->nose = _arg;
    return *this;
  }
  Type & set__eye_l(
    const std::vector<float, typename ContainerAllocator::template rebind<float>::other> & _arg)
  {
    this->eye_l = _arg;
    return *this;
  }
  Type & set__eye_r(
    const std::vector<float, typename ContainerAllocator::template rebind<float>::other> & _arg)
  {
    this->eye_r = _arg;
    return *this;
  }
  Type & set__ear_l(
    const std::vector<float, typename ContainerAllocator::template rebind<float>::other> & _arg)
  {
    this->ear_l = _arg;
    return *this;
  }
  Type & set__ear_r(
    const std::vector<float, typename ContainerAllocator::template rebind<float>::other> & _arg)
  {
    this->ear_r = _arg;
    return *this;
  }
  Type & set__shoulder_l(
    const std::vector<float, typename ContainerAllocator::template rebind<float>::other> & _arg)
  {
    this->shoulder_l = _arg;
    return *this;
  }
  Type & set__shoulder_r(
    const std::vector<float, typename ContainerAllocator::template rebind<float>::other> & _arg)
  {
    this->shoulder_r = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    sunflower_interfaces::msg::TfliteResult_<ContainerAllocator> *;
  using ConstRawPtr =
    const sunflower_interfaces::msg::TfliteResult_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sunflower_interfaces::msg::TfliteResult_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sunflower_interfaces::msg::TfliteResult_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sunflower_interfaces::msg::TfliteResult_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sunflower_interfaces::msg::TfliteResult_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sunflower_interfaces::msg::TfliteResult_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sunflower_interfaces::msg::TfliteResult_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sunflower_interfaces::msg::TfliteResult_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sunflower_interfaces::msg::TfliteResult_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sunflower_interfaces__msg__TfliteResult
    std::shared_ptr<sunflower_interfaces::msg::TfliteResult_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sunflower_interfaces__msg__TfliteResult
    std::shared_ptr<sunflower_interfaces::msg::TfliteResult_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TfliteResult_ & other) const
  {
    if (this->nose != other.nose) {
      return false;
    }
    if (this->eye_l != other.eye_l) {
      return false;
    }
    if (this->eye_r != other.eye_r) {
      return false;
    }
    if (this->ear_l != other.ear_l) {
      return false;
    }
    if (this->ear_r != other.ear_r) {
      return false;
    }
    if (this->shoulder_l != other.shoulder_l) {
      return false;
    }
    if (this->shoulder_r != other.shoulder_r) {
      return false;
    }
    return true;
  }
  bool operator!=(const TfliteResult_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TfliteResult_

// alias to use template instance with default allocator
using TfliteResult =
  sunflower_interfaces::msg::TfliteResult_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace sunflower_interfaces

#endif  // SUNFLOWER_INTERFACES__MSG__DETAIL__TFLITE_RESULT__STRUCT_HPP_
