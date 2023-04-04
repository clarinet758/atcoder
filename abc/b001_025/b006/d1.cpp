#include <iostream>
#include <vector>
#include <algorithm> // std::lower_bound()

/// @brief 最長増加部分列（LIS）の長さを返します（狭義単調増加）
/// @tparam Type 数列の要素の型
/// @param v 数列
/// @return 最長増加部分列（LIS）の長さ
/// @note 1.1 最長増加部分列の長さの取得（狭義単調増加）
/// @see https://zenn.dev/reputeless/books/standard-cpp-for-competitive-programming/viewer/lis
template <class Type>
size_t LIS(const std::vector<Type>& v)
{
	std::vector<Type> dp;

	for (const auto& elem : v)
	{
		auto it = std::lower_bound(dp.begin(), dp.end(), elem);

		if (it == dp.end())
		{
			dp.push_back(elem);
		}
		else
		{
			*it = elem;
		}
	}

	return dp.size();
}

int main()
{
	int N;
	std::cin >> N;

	std::vector<int> A(N);
	for (auto& a : A)
	{
		std::cin >> a;
	}

	std::cout << N-LIS(A) << '\n';
}