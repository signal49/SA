package main
import (
	"fmt"
	"strings"
	"strconv"

)
type Codec struct {
	b strings.Builder
}

// Encodes a list of strings to a single string.
func (codec *Codec) Encode(strs []string) string {
	defer codec.b.Reset()

	for _, word := range strs {
		codec.b.WriteString(strconv.Itoa(len(word)))
		codec.b.WriteRune('|')
		codec.b.WriteString(word)
	}

	return codec.b.String()
}

// Decodes a single string to a list of strings.
func (codec *Codec) Decode(strs string) []string {
	var words []string

	for i := 0; i < len(strs);  {
		lenStart := i
		lenEnd := i

		for strs[lenEnd] != '|' {
			lenEnd++
		}

		var l int
		dec := 1

		for j := lenEnd - 1; j >= lenStart; j-- {
			l += (int(strs[j]) - 48) * dec
			dec *= 10
		}

		start := lenEnd + 1
		end := start + l

		words = append(words, string(strs[start:end]))

		i = end
	}

	return words
}


func main(){
	
	//encode decode
	st := []string{"bud", "dog", "surf", "summer"}
	fmt.Println(Encode(st))
	
	
	//nums := []int{1, 1, 1, 2, 2, 3}
	//k := 2
	//fmt.Println(topKFrequent(nums, k)) // Output: [1 2]
	
	//anagram groups
	//ag := []string{"act", "pots", "tops", "cat", "stop", "hat"}
	//fmt.Println(groupAnagrams(ag))

	//twosum
	//nums := []int{2,7,11,15}
	//target := 9
	//fmt.Println(twoSum(nums, target))
	
	//valid anagram
	//fmt.Println(isAnagram("anagram", "nagaram")) // Example usage

	//contains duplicate
	//nums := []int{1,2,3,1}
	//fmt.Println(containsDup(nums))//output: true

	
}
//CodeConvert.ai
//Neetcode.io/practice
//Arrays & Hashing
//lc#217
func containsDup(nums []int) bool{
	hashset := make(map[int] struct{})
	if len(nums) <= 1{
		return false
	}
		
	for _, n := range nums{
		if _, exists := hashset[n]; exists{
			return true
		}
		hashset[n] = struct{}{}
	}
	return false
}

//lc242-valid anagram
func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    countS := make(map[rune]int)
    countT := make(map[rune]int)

    for i := 0; i < len(s); i++ {
        countS[rune(s[i])]++
        countT[rune(t[i])]++
    }
    return equalMaps(countS, countT)
}

func equalMaps(a, b map[rune]int) bool {
    if len(a) != len(b) {
        return false
    }
    for k, v := range a {
        if b[k] != v {
            return false
        }
    }
    return true
}

//twoSum
func twoSum(nums []int, target int) []int {
    prevMap := make(map[int]int) // val -> index

    for i, n := range nums {
        diff := target - n
        if index, found := prevMap[diff]; found {
            return []int{index, i}
        }
        prevMap[n] = i
    }
    return nil
}

//group anagrams
func groupAnagrams(strs []string) [][]string {
    anagramMap := make(map[[26]int][]string)
    for _, s := range strs {
        var count [26]int
        for _, c := range s {
            count[c - 'a']++
        }
        anagramMap[count] = append(anagramMap[count], s)
    }
    result := make([][]string, len(anagramMap))
    idx := 0
    for _, v := range anagramMap {
        result[idx] = v
        idx++
    }
    return result
}

//top K frequent
func topKFrequent(nums []int, k int) (res []int ){
	countMap := map[int]int{}
	countSlice := make([][]int, len(nums)+1)

	for _, num := range nums {
		if count, ok := countMap[num]; ok {
			countMap[num] = count + 1
		} else {
			countMap[num] = 1
		}
	}

	for num, count := range countMap {
		countSlice[count] = append(countSlice[count], num)
	}

	for i := len(countSlice) - 1; i > 0; i-- {
		res = append(res, countSlice[i]...)
		if len(res) == k {
			return
		}
	}

	return
}



